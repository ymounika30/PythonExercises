##WAP to find the number is strong number or not  
def factorial(y):
    if y==1:
        return y
    else:
        return y*factorial(y-1)
a=int(input())
x=str(a)
b=0
for i in x:
    y=int(i)
    t=factorial(y)
    b=b+t
if a==b:
    print("strong number")
else:
    print("Not strong number")
