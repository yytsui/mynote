
from datetime import datetime
import pytz

TIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z%z"

def convert_timezone(to_tz, dt):
    """
    get to_tz identifier from:
       http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    dt: datetime object
    """
    _to_tz = pytz.timezone(to_tz)
    dt_to = _to_tz.normalize(dt.astimezone(_to_tz))
    return dt_to


def test_now():
    #The preferred way of dealing with times is to always work in UTC, 
    #converting to localtime only when generating output to be read by humans.
    dt_now = datetime.now() #naive datetime object
    print dt_now.strftime(TIME_FORMAT)
    pacific = pytz.timezone('US/Pacific')
    dt_now_aware = pacific.localize(dt_now)
    print dt_now_aware.strftime(TIME_FORMAT)
    dt_now_converted = convert_timezone('US/Eastern', dt_now_aware)
    print dt_now_converted.strftime(TIME_FORMAT)
    timediff = dt_now_converted - dt_now_aware
    assert timediff.total_seconds() == 0

    print dt_now_aware.hour
    print dt_now_converted.hour


if __name__ == '__main__':
    test_now()
