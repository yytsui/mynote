
from datetime import datetime
import pytz #run "pip install pytz" if you have not installed it yet.

TIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z%z"

def convert_timezone(from_tz, to_tz, dt):
    """
    get from_tz, to_tz identifier from:
       http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    dt: datetime object
    """
    _from_tz = pytz.timezone(from_tz)
    dt_from_aware = _from_tz.localize(dt)
    _to_tz = pytz.timezone(to_tz)
    dt_to_aware = _to_tz.normalize(dt_from_aware.astimezone(_to_tz))
    return dt_from_aware, dt_to_aware


def test_now():
    """
    The preferred way of dealing with times is to always work in UTC, 
    converting to localtime only when generating output to be read by humans.
    http://pytz.sourceforge.net/
    """
    dt_now = datetime.now() #naive datetime object
    dt_from_aware, dt_to_aware = convert_timezone('Canada/Pacific', 'Canada/Eastern',dt_now)
    timediff = dt_to_aware - dt_from_aware
    assert timediff.total_seconds() == 0
    assert dt_to_aware.hour - dt_from_aware.hour == 3
    print dt_from_aware.strftime(TIME_FORMAT)
    print dt_to_aware.strftime(TIME_FORMAT)

def test_parse_time():
    """
    test parsing from string:2013-05-23T15:36:27
    """
    timestr = "2013-05-23T15:36:27"
    dt = datetime.strptime(timestr,"%Y-%m-%dT%H:%M:%S")
    dt_from_aware, dt_to_aware = convert_timezone('Canada/Mountain', 'Canada/Eastern',dt)
    timediff = dt_to_aware - dt_from_aware
    assert timediff.total_seconds() == 0
    assert dt_to_aware.hour - dt_from_aware.hour == 2
    print dt_from_aware.strftime(TIME_FORMAT)
    print dt_to_aware.strftime(TIME_FORMAT)


if __name__ == '__main__':
    test_now()
    test_parse_time()
