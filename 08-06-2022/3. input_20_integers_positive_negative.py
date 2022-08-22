##3.
##Take 20 integer inputs from user and print the following:
##number of positive numbers
##number of negative numbers
##number of odd numbers
##number of even numbers
##number of 0s
a=int(input())
list_a=[]
x=0
y=0
z=0
p=0
q=0
for i in range(a):
    b=int(input())
    list_a+=[b]
print(list_a)
for m in list_a:
    if m>0:
        x=x+1
    if m<0:
        y=y+1
    if (m%2)==0:
        z=z+1
    if (m%2)==1:
        p=p+1
    if m==0:
        q=q+1
print(x)
print(y)
print(z)
print(p)
print(q)
