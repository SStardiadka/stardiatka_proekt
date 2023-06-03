""" работа с датой """
from datetime import datetime, timedelta, date

print(date.today())  # 2023-05-31
d = date.today()
delta = timedelta(days=3)
print(d + delta)  # 2023-06-03
print(datetime.now())  # 2023-05-31 22:07:42.595658
