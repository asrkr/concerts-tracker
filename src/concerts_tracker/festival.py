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
