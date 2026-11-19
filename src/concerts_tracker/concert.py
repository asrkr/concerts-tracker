"""Concert model."""

from dataclasses import dataclass
from datetime import date, datetime, time


@dataclass
class Concert:
    """A concert: one artist performing at a venue on a given day and time."""
    artist: str
    day: date
    start_time: time
    venue: str
    opening_act: str | None = None

    @property
    def complete_date(self) -> datetime:
        """Day and start time of the concert as a single datetime."""
        return datetime.combine(self.day, self.start_time)

    @property
    def is_past(self) -> bool:
        """Whether the concert has already started."""
        return datetime.now() > self.complete_date
