import os
import textwrap
from time import time
from typing import Callable

import thirdai
import thirdai._distributed_bolt.backend.communication as comm
from thirdai._thirdai import bolt, bolt_v2, logging

from ..utils import timed


class Worker:
    """
    This is a ray remote class(Actor). Read about them here.
    (https://docs.ray.io/en/latest/ray-core/actors.html)

    Worker is a ray actor which implements all the lower level
    functionalities between the Distributed Bolt APIs and
    Bolt native code.
    """

    @timed
    def __init__(
        self,
        num_workers: int,
        model_lambda: Callable[[], bolt.nn.Model],
        licensing_lambda: Callable[[], None],
        train_source,
        id: int,
        primary_worker,
        train_config: bolt.TrainConfig,
        communication_type: str,
        log_dir: str,
    ):
        """
        Initializes the worker, including wrapping the passed in model in a
        DistributedWrapper with the dataset read in.
        """

        # These next two steps are necessary to satisfy our licensing system.
        # Deserializing a model requires a valid license, so we can't pass the
        # model directly in to the constructor. Instead, we pass in a lambda
        # that we run to initialize licensing, then a lambda that we call to
        # get and deserialize the model.
        licensing_lambda()
        model_to_wrap = model_lambda()

        self.train_source = train_source
        self.train_source.load()

        self.num_workers = num_workers
        self.id = id
        self.primary_worker = primary_worker
        self.communication_type = communication_type

        logging.setup(
            log_to_stderr=False, path=os.path.join(log_dir, f"worker-{id}.log")
        )

        logging.info(f"sub_task initializing_model on worker-{id}")
        start = time()
        # TODO(Nick): Remove hasattr check
        DistributedTrainingWrapper = (
            bolt_v2.train.DistributedTrainingWrapper
            if hasattr(bolt_v2, "nn") and isinstance(model_to_wrap, bolt_v2.nn.Model)
            else bolt.DistributedTrainingWrapper
        )
        self.model = DistributedTrainingWrapper(
            model=model_to_wrap,
            train_config=train_config,
            worker_id=id,
        )
        end = time()

        logging.info(f"sub_task initialized_model | time {(end - start)*1000} ms")

        start = time()
        if self.communication_type == "circular":
            self.comm = comm.Circular(
                self.model, self.id, self.primary_worker, self.num_workers
            )
        elif self.communication_type == "linear":
            self.comm = comm.Linear(self.model, self.id, self.primary_worker)
        elif self.communication_type == "gloo":
            # We are using "default", as a global group name for all the workers, as
            # right now, we connect all the worker in one cluster
            self.comm = comm.Gloo(self.model, self.id, self.num_workers, "default")
        else:
            raise ValueError(
                textwrap.dedent(
                    """
                        Currently only three modes of communication are supported.
                        Use: "circular" or "linear" or "gloo". 
                    """
                )
            )
        end = time()
        logging.info(
            f"sub_task communication_intialized | time {(end - start)*1000} ms"
        )

        if not self._try_load_new_datasets_into_model():
            raise ValueError(
                "There must be at least one loadable dataset in the passed in data source."
            )

    # see https://github.com/ray-project/ray/blob/4b59dfbe59a143ab8dcc505dad860b4c330b6426/python/ray/actor.py#L1183
    # It looks like ray doesnot support direct class attribute access in python.
    # Hence, we will need to expose this function here in worker
    def set_friend(self, friend):
        """
        Add the friend for communicating for cicrcular all reduce

        :param friend: worker to which self need to communication
                            for circular all reduce
        :type friend: ray.actor
        """
        self.comm.set_friend(friend)

    @timed
    def process_ring(
        self,
        update_id: int,
        reduce: bool = True,
        avg_gradients: bool = False,
    ):
        """
        This function handles the circular all reduce

        :param update_id: The update sequence id
        :type update_id: int
        :param reduce: True if reduce, False if gather, defaults to True
        :type reduce: bool
        :param avg_gradients: whether the update requires updating the gradients, defaults to False
        :type avg_gradients: bool
        """
        self.comm.process_ring(update_id, reduce, avg_gradients)

    @timed
    def receive_array_partitions(self, update_id: int):
        """
        This function returns the array partition for the worker is is called.

        :param update_id: The update sequence id
        :type update_id: int
        :return: subarray partition
        :rtype: numpy.ndarray
        """
        return self.comm.receive_array_partitions(update_id)

    @timed
    def compute_and_store_next_batch_gradients(self) -> bool:
        """
        Computes and stores the gradients on all nodes. After this returns,
        all nodes are ready to communicate gradients. Returns whether this
        worker has another batch.
        """
        if self.datasets == None or self.model.num_batches() == 0:
            raise ValueError(
                "Cannot call train when we have run out of training data (this function has previously returned False without a subsequent call to move_to_next_epoch())"
            )
        self.comm.compute_and_store_batch_gradients(self.batch_id_within_dataset)

        self.batch_id_within_dataset += 1
        if self.batch_id_within_dataset == self.model.num_batches():
            return self._try_load_new_datasets_into_model()

        elif self.batch_id_within_dataset > self.model.num_batches():
            raise ValueError(
                "Found a batch id higher than the number of batches which we should have caught during the last batch."
            )
        else:
            return True

    @timed
    def move_to_next_epoch(self):
        self.train_source.restart()
        self._try_load_new_datasets_into_model()
        self.model.increment_epoch_count()

    @timed
    def get_calculated_gradients(self):
        """
        This function is called only when the mode of communication
        is Linear.

        This function is called by the primary_worker to compute the
        averages of the calculated gradients. This functions
        calls 'get_weights_gradient' and 'get_biases_gradients' functions
        inside bolt to take the gradients and return them to primary_worker.

        :return: Model Gradients
        :rtype: numpy.ndarray
        """
        return self.model.gradient_reference().get_gradients()

    @timed
    def receive_gradients(self, averaged_gradients_ref=None):
        """
        This function is called only when the communication pattern choosen
        is circular.

        This function is called by the primary_worker to make set the updated
        gradients to the network.

        :param averaged_gradients_ref: gets the references for averaged gradients
                    for linear communication, defaults to None for any other way
                    to communicate
        :type averaged_gradients_ref: RayObjectRef, optional
        """
        if self.communication_type != "linear":
            self.comm.receive_gradients()
        else:
            self.comm.receive_gradients(averaged_gradients_ref)

    @timed
    def _try_load_new_datasets_into_model(self) -> bool:
        """
        Returns whether the load was successful (if the generator stream is over
        then this will fail until we call restart on it).
        """

        self.datasets = self.train_source.next()

        if self.datasets == None:
            return False

        self.model.set_datasets(self.datasets)
        self.batch_id_within_dataset = 0

        # This case should not be true since we currently require datasets
        # to be nonempty, but this is a good hedge against future data
        # pipeline changes
        if self.model.num_batches() == 0:
            return False

        return True

    @timed
    def update_parameters(self):
        """
        This function calls updateParameter function inside bolt, which
        inherently updates the entire network.
        """
        self.model.update_parameters()

    def num_of_batches(self):
        """
        This function returns the total number of batches the workers have.
        """
        return self.model.num_batches()

    def freeze_hash_tables(self):
        self.model.freeze_hash_tables(True)

    def get_updated_metrics(self):
        return self.model.get_updated_metrics()

    def update_learning_rate(self, learning_rate):
        self.model.update_learning_rate(learning_rate)

    def model(self, with_optimizer):
        # setting with_optimizer flag, here implies that model would be serialized/pickled with optimizer. It is similar to how save/checkpoint works as pickling also uses cereal.
        if with_optimizer:
            self.model.should_save_optimizer(True)
        return self.model.model
