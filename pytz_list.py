import pytz

def pytz_list():
    timezones = pytz.all_timezones
    count = 0
    timezones_count = len(timezones)
    while count <= timezones_count:
        for tz in timezones:
            print(count, tz)
            count += 1