import datetime
mytime = datetime.time(2)
print(mytime.minute)
print(mytime.hour)
print(mytime)

today = datetime.date.today()
print(today)
today.year
today.ctime()
#'Fri Jun 12 00:00:00 2020'

from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)

mydatetime = mydatetime.replace(year=2020)

# Date
from datetime import date
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

print(date1 - date2)

mydiff = date1 - date2
mydiff.total_seconds
