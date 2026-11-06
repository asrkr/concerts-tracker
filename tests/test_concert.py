from concerts_tracker.concert import Concert
from datetime import date, time, datetime, timedelta


def test_concert_creation() -> None:
    concert_test = Concert(artist="Lana Del Rey", day=date(2024, 8, 21), start_time=time(21, 30), venue="Rock En Seine")
    assert concert_test.artist == "Lana Del Rey"
    assert concert_test.venue == "Rock En Seine"
    assert concert_test.complete_date == datetime(2024, 8, 21, 21, 30)
    assert concert_test.is_past


def test_concert_is_not_past() -> None:
    tomorrow = date.today() + timedelta(days=1)
    concert_test = Concert(artist="Noah Kahan", day=tomorrow, start_time=time(20, 0), venue="Accor Arena")
    assert not concert_test.is_past 
