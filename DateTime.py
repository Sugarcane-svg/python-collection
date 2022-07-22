# date time usage and manupulation, time delta, and fString usage.



import datetime
import time

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

time.sleep(10)

later = datetime.datetime.now()
print(later)
print(f"the difference between now and later is {later - now}")