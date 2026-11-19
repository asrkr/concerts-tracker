"""Concert class, is reused in Festival class."""

from dataclasses import dataclass
from datetime import date, datetime, time


@dataclass
class Concert:
    """An event, with one artist, a day, time and place."""
    artist: str
    day: date
    start_time: time
    venue: str
    opening_act: str | None = None

    @property
    def complete_date(self) -> datetime:
        """Combines the day and the time to create a datetime object."""
        return datetime.combine(self.day, self.start_time)

    @property
    def is_past(self) -> bool:
        """"Checks if a concert has already happened."""
        return datetime.now() > self.complete_date
