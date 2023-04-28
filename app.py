from astral.sun import sun
from astral import LocationInfo
from datetime import date, timedelta, datetime, timezone
import sched
import time
import pytz

s = sched.scheduler(time.time, time.sleep)

LOCATION = LocationInfo("Boston", "US", "US/Eastern", 42.3601, -71.0589)
tz=pytz.timezone(LOCATION.timezone)
START_DAY = datetime(2023, 4, 1, tzinfo=tz)
END_DAY = datetime(2024, 5, 1, tzinfo=tz)
CLIP_LENGTH = 1

times = []

def take_video():
  print("Taking video")

def set_times():
  num_days = (END_DAY - START_DAY).days

  for i in range(num_days):
    day = START_DAY + timedelta(days=i)
    sun_info = sun(LOCATION.observer, date=day)
    
    sunrise = sun_info["sunrise"]
    sunset = sun_info["sunset"]
    day_length = sunset - sunrise
    day_wait = day_length * (i / (num_days - 1))

    picture_time = sunrise + day_wait

    times.append(picture_time)

def schedule_times():
  now = time.time()
  for t in times:
    epoch = t.timestamp()
    if epoch > now:
      s.enterabs(t.timestamp(), 1, take_video)
  s.run()


set_times()
schedule_times()
