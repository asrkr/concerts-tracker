from dataclasses import dataclass
from datetime import date, time, datetime


@dataclass
class Concert:
    artist: str
    day: date
    start_time: time
    venue: str
    opening_act: str | None = None

    @property
    def complete_date(self) -> datetime:
        return datetime.combine(self.day, self.start_time)

    @property
    def is_past(self) -> bool:
        return datetime.now() > self.complete_date
