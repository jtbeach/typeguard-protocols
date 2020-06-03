"""Example code showing typeguard failure."""
from abc import abstractmethod
from typing import Protocol


class Impl(Protocol):
    """Typing protocols for GCS buckets so that we can mock."""

    @abstractmethod
    def name(self) -> str:
        pass


def handle_impl(impl: Impl) -> str:
    """Handle an object that follows the Impl protocol."""
    return impl.name()
