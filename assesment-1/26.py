##26. Write a Python program to count most and least common characters in a given string
a=input()
b=[]
c=[]
for i in set(a):
    b.append(i)
    c.append(a.count(i))
print(c)
y=dict(zip(b,c))
print(min(y))
print(max(y))
