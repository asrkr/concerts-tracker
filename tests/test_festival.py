"""Tests for the Festival model."""

from datetime import date, time

from concerts_tracker.concert import Concert
from concerts_tracker.festival import Festival


def test_festival_creation() -> None:
    """A festival keeps the concerts it is created with."""
    concert1 = Concert(
        artist="Noah Kahan",
        day=date(2025, 12, 7),
        start_time=time(20, 0),
        venue="Accor Arena",
    )
    concert2 = Concert(
        artist="Lana Del Rey",
        day=date(2025, 12, 7),
        start_time=time(18, 0),
        venue="Accor Arena",
    )
    festival = Festival(name="DreamFest", concerts=[concert1, concert2])
    assert len(festival.concerts) == 2


def test_festival_is_empty_by_default() -> None:
    """A festival created with only a name has no concerts and no dates."""
    festival = Festival(name="Hellfest")
    assert not festival.concerts
    assert festival.start_date is None
    assert festival.end_date is None


def test_festival_start_end_date() -> None:
    """start_date and end_date are the earliest and latest concert days."""
    concert1 = Concert(
        artist="David Guetta",
        day=date(2027, 6, 13),
        start_time=time(20, 0),
        venue="Hippodrome de Longchamp",
    )
    concert2 = Concert(
        artist="Zara Larsson",
        day=date(2027, 6, 14),
        start_time=time(19, 0),
        venue="Hippodrome de Longchamp",
    )
    festival = Festival(name="Solidays", concerts=[concert1, concert2])
    assert festival.start_date == concert1.day
    assert festival.end_date == concert2.day
