"""Festival class. A list of concerts, with a place and start/end dates."""

from dataclasses import dataclass, field
from datetime import date

from concerts_tracker.concert import Concert


@dataclass
class Festival:
    """An event regrouping multiple concerts in one place."""
    name: str
    concerts: list[Concert] = field(default_factory=list)

    @property
    def start_date(self) -> date | None:
        """Returns the date of the earliest show."""
        days = [concert.day for concert in self.concerts]
        return min(days, default=None)

    @property
    def end_date(self) -> date | None:
        """Returns the date of the latest show."""
        days = [concert.day for concert in self.concerts]
        return max(days, default=None)
