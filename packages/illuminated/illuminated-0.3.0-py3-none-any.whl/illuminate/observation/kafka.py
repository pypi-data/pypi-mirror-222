from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any, Callable, Optional, Union

from aiokafka import AIOKafkaConsumer  # type: ignore
from aiokafka.errors import KafkaError  # type: ignore
from loguru import logger

from illuminate.meta.type import Result
from illuminate.observation import Observation


class KafkaObservation(Observation):
    """
    KafkaObservation class, reads kafka messages asynchronously. Inherits
    Observation class and implements observe method.
    """

    def __hash__(self) -> int:
        """
        KafkaObservation object hash value.

        :return: int
        """
        return hash(f"{self.url}|{self.topics}")

    def __init__(
        self,
        topics: tuple[str],
        url: str,
        /,
        callback: Callable[[AIOKafkaConsumer, tuple, dict], Result],
        xcom: Optional[Any] = None,
        *args,
        **kwargs,
    ):
        """
        KafkaObservation's __init__ method.

        :param url: Kafka server URL
        :param callback: Async function/method that manipulates
        AIOKafkaConsumer object and returns Result
        :param topics: Tuple of Kafka topics
        :param xcom: Cross communication object
        """
        super().__init__(url, xcom=xcom)
        self._callback = callback
        self.configuration = kwargs
        self.topics = topics

    @asynccontextmanager
    async def observe(
        self, *args, **kwargs
    ) -> AsyncIterator[Union[None, Result]]:
        """
        Opens connection to Kafka server, pass AIOKafkaConsumer object to a
        callback and returns None or Result as a context manager.

        :return: AsyncIterator with None or Result
        """
        consumer = AIOKafkaConsumer(
            *self.topics, bootstrap_servers=self.url, **self.configuration
        )
        await consumer.start()
        try:
            yield self._callback(consumer, *args, **kwargs)
        except KafkaError as exception:
            logger.warning(f"{self}.observe() -> {exception}")
            yield None
        except Exception as exception:
            logger.critical(f"{self}.observe() -> {exception}")
            yield None
        finally:
            logger.debug(True)
            await consumer.stop()

    def __repr__(self):
        """
        KafkaObservation's __repr__ method.

        :return: String representation of an instance
        """
        return (
            f'KafkaObservation("{self.url}",callback="{self._callback}",'
            f'topics="{self.topics}")'
        )
