from dataclasses import dataclass, field
from datetime import date

from concerts_tracker.concert import Concert


@dataclass
class Festival:
    name: str
    concerts: list[Concert] = field(default_factory=list)

    @property
    def start_date(self) -> date | None:
        days = [concert.day for concert in self.concerts]
        return min(days, default=None)

    @property
    def end_date(self) -> date | None:
        days = [concert.day for concert in self.concerts]
        return max(days, default=None)
