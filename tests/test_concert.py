"""Tests for the Concert model."""

from dataclasses import replace
from datetime import date, datetime, timedelta

from concerts_tracker.concert import Concert


def test_concert_creation(concert: Concert) -> None:
    """A past concert exposes its fields, complete_date and is_past."""
    assert concert.artist == "Lana Del Rey"
    assert concert.venue == "Domaine de Saint-Cloud"
    assert concert.complete_date == datetime(2024, 8, 21, 21, 0)
    assert concert.is_past


def test_concert_is_not_past(concert: Concert) -> None:
    """A concert scheduled for tomorrow is not past."""
    upcoming = replace(concert, day=date.today() + timedelta(days=1))
    assert not upcoming.is_past
