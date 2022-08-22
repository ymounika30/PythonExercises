##Python Program to Find Armstrong Number in an Interval 
a=int(input())
b=int(input())
s=""
for i in range(a,b+1):
    x=str(i)
    y=len(x)
    c=0
    for j in range(y):
        c=c+(int(x[j])**y)
    if (c==i):
        s=s+x+" "
if s==" ":
    print("-1")
print(s)
