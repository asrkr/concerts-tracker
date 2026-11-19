"""Shared fixtures for the test suite."""

from datetime import date, time

import pytest

from concerts_tracker.concert import Concert
from concerts_tracker.festival import Festival


@pytest.fixture
def concert() -> Concert:
    """A sample concert."""
    return Concert(
        artist="Lana Del Rey",
        day=date(2024, 8, 21),
        start_time=time(21, 0),
        venue="Domaine de Saint-Cloud",
    )


@pytest.fixture
def festival() -> Festival:
    """An empty festival."""
    return Festival(name="DreamFest")
