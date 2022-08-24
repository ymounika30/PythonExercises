##29. Write a Python program to convert a list into a nested dictionary of keys

a=[1, 2, 3, 4]
b=current={}
for i in a:
    current[i]={}
    current = current[i]
print(b)
