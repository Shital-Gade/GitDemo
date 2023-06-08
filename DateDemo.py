import datetime
from datetime import date

mytime = datetime.time(2, 20)

print(mytime.hour)

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())

date1=date(2023, 5, 30)
date2= date(2022, 11, 15)
result= date1-date2
print(result)
print(type(result))