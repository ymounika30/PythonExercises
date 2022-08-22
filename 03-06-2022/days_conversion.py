a=997
year=a//365
a=a%365
month=a//30
a=a%30
week=a//7
a=a%7
print(str(year)+" years "+ str(month) +" months " + str(week) +" weeks " + str(a)+" days ")
