"""Tests for the Festival model."""

from datetime import time, timedelta
from dataclasses import replace

import pytest

from concerts_tracker.concert import Concert
from concerts_tracker.festival import Festival


def test_festival_creation(concert: Concert) -> None:
    """A festival keeps the concerts it is created with."""
    other = replace(concert, artist="Noah Kahan", start_time=time(18, 0))
    festival = Festival(name="DreamFest", concerts=[concert, other])
    assert len(festival.concerts) == 2


def test_festival_is_empty_by_default(festival: Festival) -> None:
    """A festival created with only a name has no concerts and no dates."""
    assert not festival.concerts
    assert festival.start_date is None
    assert festival.end_date is None


def test_festival_start_end_date(concert: Concert) -> None:
    """start_date and end_date are the earliest and latest concert days."""
    next_day = replace(concert, artist="Zara Larsson", day=concert.day + timedelta(days=1))
    festival = Festival(name="Solidays", concerts=[next_day, concert])
    assert festival.start_date == concert.day
    assert festival.end_date == next_day.day


def test_add_concert_appends_to_festival(festival: Festival, concert: Concert) -> None:
    """add_concert adds the concert to the festival's list."""
    festival.add_concert(concert)
    assert festival.concerts == [concert]


def test_add_concert_rejects_same_start(festival: Festival, concert: Concert) -> None:
    """add_concert refuses a concert starting at the same time as another one."""
    festival.add_concert(concert)
    clash = replace(concert, artist="Noah Kahan")
    with pytest.raises(ValueError):
        festival.add_concert(clash)
    assert festival.concerts == [concert]
