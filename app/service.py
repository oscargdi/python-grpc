import abc
import logging

from loguru import logger


class Service(abc.ABC):
    """Service interface."""

    @abc.abstractmethod
    def get_greeting(self, name: str) -> str:
        """Return greeting."""


class GreeterService(Service):
    """Greeter service implementation."""

    @logger.catch(reraise=True)
    def get_greeting(self, name: str):
        logger.info("Calling implementation")
        raise Exception("This error is not being reported :(")
        return f"Hello {name}"
