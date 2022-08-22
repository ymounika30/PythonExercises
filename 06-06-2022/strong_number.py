
num=int(input("Enter a number:"))
b=0
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    b=b+f
    num=num//10
if(b==temp):
    print("strong number")
else:
    print("Not a strong number")
