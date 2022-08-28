from datetime import datetime
from loguru import logger as log


def get_tz_name():
    now = datetime.now()
    local_now = now.astimezone()
    local_tz = local_now.tzinfo
    local_tzname = local_tz.tzname(local_now)
    print(local_tzname)