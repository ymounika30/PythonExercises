##2. Write a Python program to extract year, month, date and time using Lambda. 
import datetime
x = datetime.datetime.now()
print(x)
year=lambda a: a.year
month=lambda a: a.month
day=lambda a: a.day
t=lambda a: a.time()
print(year(x))
print(month(x))
print(day(x))
