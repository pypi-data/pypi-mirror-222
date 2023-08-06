import multiprocessing as mp
import sys

try:
    from faster_fifo import Queue as FasterQueue  # type: ignore
except ImportError:
    raise ImportError("Install whylogs with extra [proc] for process based logging: pip install whylogs[proc]")
from typing import Generic, List, Optional, TypeVar

from whylogs.api.logger.experimental.logger.actor.actor import (
    Actor,
    QueueConfig,
    QueueWrapper,
)

_DEFAULT_QUEUE_SiZE = 1000 * 1000 * 1000

FasterQueueMessageType = TypeVar("FasterQueueMessageType")


class FasterQueueWrapper(QueueWrapper, Generic[FasterQueueMessageType]):
    """
    Implementation of QueueWrapper sufficient for use in the threaded actor.
    """

    def __init__(self) -> None:
        self._queue = FasterQueue(_DEFAULT_QUEUE_SiZE)

    def send(self, message: FasterQueueMessageType, timeout: float = 0.1) -> None:
        self._queue.put(message, timeout=timeout)

    def send_many(self, messages: List[FasterQueueMessageType], timeout: float = 0.1) -> None:
        self._queue.put_many(messages, timeout=timeout)

    def get(self, timeout: float = 0.1) -> Optional[FasterQueueMessageType]:
        return self._queue.get(timeout=timeout)

    def get_many(self, timeout: float = 0.1, max: Optional[int] = None) -> List[FasterQueueMessageType]:
        return self._queue.get_many(timeout=timeout, max_messages_to_get=max)

    def size(self) -> int:
        return self._queue.qsize()

    def close(self) -> None:
        self._queue.close()


ProcessMessageType = TypeVar("ProcessMessageType")


class ProcessActor(Actor, mp.Process, Generic[ProcessMessageType]):
    """
    Subclass of Actor that uses a process to process messages.
    """

    def __init__(self, queue_config: QueueConfig = QueueConfig()) -> None:
        self._wrapper = FasterQueueWrapper[ProcessMessageType]()
        self._event = mp.Event()
        self._is_closed = mp.Event()
        # our mypy version has a false positive on this super call
        super().__init__(self._wrapper, queue_config)  # type: ignore

    def is_done(self) -> bool:
        return self._event.is_set()

    def done_wait(self) -> None:
        self._event.wait()

    def set_done(self) -> None:
        self._event.set()

    def set_closed(self) -> None:
        self._is_closed.set()

    def is_closed(self) -> bool:
        return self._is_closed.is_set()

    def close(self) -> None:
        if self.pid is None:
            raise Exception("Process hasn't been started yet.")

        super().close()
        self._wrapper.close()

    def run(self) -> None:
        super().run()
        sys.exit(0)

    def start(self) -> None:
        """
        The process version of the actor apparently has to be manually started after
        it's created, unlike the thread version which can just be automatically started
        from within its init. There must be some post-init setup that needs to be done.
        """
        self.daemon = True
        super().start()
        self.join(0.1)  # This does apparently need to happen after several manual tests.
