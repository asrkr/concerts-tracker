"""Festival model."""

from dataclasses import dataclass, field
from datetime import date

from concerts_tracker.concert import Concert


@dataclass
class Festival:
    """An named event grouping several concerts."""
    name: str
    concerts: list[Concert] = field(default_factory=list)

    @property
    def start_date(self) -> date | None:
        """Day of the earliest concert, or None if there are no concerts."""
        days = [concert.day for concert in self.concerts]
        return min(days, default=None)

    @property
    def end_date(self) -> date | None:
        """Day of the latest concert, or None if there are no concerts."""
        days = [concert.day for concert in self.concerts]
        return max(days, default=None)

    @property
    def sorted_concerts(self) -> list[Concert]:
        """Concerts of the festival in chronological order."""
        return sorted(self.concerts, key=lambda c: c.complete_date)


    def add_concert(self, concert: Concert) -> None:
        """Add a concert to the festival.

        Raises:
            ValueError: if another concert already starts at the same date and time.
        """
        if any(c.complete_date == concert.complete_date for c in self.concerts):
            raise ValueError("Un concert a déjà lieu en même temps.")
        self.concerts.append(concert)
