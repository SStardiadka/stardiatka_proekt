#  Mодуль –  datetime. Он позволяет работать с датой и временем, представляя их в понятном для человека формате UTC. 

from datetime import datetime, date

d = datetime(year=2022, month=12, day=31, hour=12, minute=12, second=30)
print(d) # 2022-12-31 12:12:30

print(d.date()) # 2022-12-31

print(date.today()) # сегодняшняя дата

d1 = datetime(year=2022, month=12, day=31, hour=12, minute=12, second=30)
d2 = datetime(year=2023, month=7, day=24, hour=16, minute=16, second=22)
print(d2 - d1) # 205 days, 4:03:52