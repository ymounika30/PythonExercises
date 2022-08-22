##import datetime
##content=dir(datetime)
##print(content)

##output:
##['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__',
## '__doc__', '__file__', '__loader__', '__name__', '__package__',
## '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time',
## 'timedelta', 'timezone', 'tzinfo']

"""1)display the current date."""
##import datetime
##x=datetime.datetime.now()
##print(x)


"""2)create a date object."""
##import datetime
##x=datetime.datetime(2022,6,7)
##print(x)



"""3)print the present year and today dayname"""
##import datetime
##x=datetime.datetime.now()
##print(x.year)
##print("today name is short name of week={}".format(x.strftime("%a")))
##print("today name is full name of week={}".format(x.strftime("%A")))


"""4)print the present month"""
##import datetime
##x=datetime.datetime.now()
##print("present month is short name of={}".format(x.strftime("%b")))
##print("present month is full name of={}".format(x.strftime("%B")))

"""5)print the weekday number """
"""ex: weekday as a number 0-6, 0 is sunday"""
##import datetime
##x=datetime.datetime.now()
##print(x.strftime("%w"))

"""6)print the today date"""
##import datetime
##x=datetime.datetime.now()
##print("today date is={}".format(x.strftime("%d")))
##print("present month number={}".format(x.strftime("%m")))
##print("present year short ={}".format(x.strftime("%y")))
##print("present year full ={}".format(x.strftime("%Y")))
##print("present (1-24)hours ={}".format(x.strftime("%H")))
##print("present (1-12) hours ={}".format(x.strftime("%I")))
##print("present am/pm ={}".format(x.strftime("%p")))
##print("present minutes ={}".format(x.strftime("%M")))
##print("present seconds ={}".format(x.strftime("%S")))
##print("present day (1-366) ={}".format(x.strftime("%j")))
##print("present week number ={}".format(x.strftime("%W")))
##print("local version of the date and time ={}".format(x.strftime("%c")))
##print("present century ={}".format(x.strftime("%C")))
##print("local version of date ={}".format(x.strftime("%x")))
##print("local version of time ={}".format(x.strftime("%X")))
