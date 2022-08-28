import pytz
from datetime import datetime, timezone

def run():
    
    now_utc = datetime.now(timezone.utc)
    local_tz = now_utc.tzinfo
    local_tzname = local_tz.tzname(now_utc)
    print(local_tzname)

if __name__ == '__main__':
   run()