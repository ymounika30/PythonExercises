##2) Write a Python program to split a given dictionary of lists into list of dictionaries.
marks={
    "Science":[88,89,62,95],
    "Language":[77,78,84,80]
    }
print(marks)
x=map(dict,zip(*[[(key,val) for val in value]for key,value in marks.items()]))
print(list(x))
