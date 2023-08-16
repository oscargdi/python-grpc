import abc
import logging

logger = logging.getLogger(__name__)


class Service(abc.ABC):
    """Service interface."""

    @abc.abstractmethod
    def get_greeting(self, name: str) -> str:
        """Return greeting."""


class GreeterService(Service):
    """Greeter service implementation."""

    def get_greeting(self, name: str):
        return f"Hello {name}"
