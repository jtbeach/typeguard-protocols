"""Example mock."""

from typeguard_test import handle_impl


class FakeImpl:
    """A mock instance of a Google Cloud Storage bucket."""

    _name: str

    def __init__(self, name: str):
        """Create a reference to a bucket in the fake google cloud storage."""
        self._name = name

    def name(self) -> str:
        return self._name


def test_fake():
    """Test that FakeImpl passes typeguard checks."""
    assert handle_impl(FakeImpl("Hello World")) == "Hello World"
