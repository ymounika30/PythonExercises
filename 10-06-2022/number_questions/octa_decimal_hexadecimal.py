##Python Program to Convert Decimal to Binary, Octal and Hexadecimal 
a=int(input())
b=""
x=a
while (x>0):
    k=x%2
    b=str(k)+b
    x=int(x/2)
print(b)
c=""
y=a
while (y>0):
    p=y%8
    c=str(p)+c
    y=int(y/8)
print(c)
d=""
z=a
while (z>0):
    q=z%16
    d=str(q)+d
    z=int(z/16)
if int(d)>=0 and int(d)<10:
    print(d)
elif (int(d)>=0) and (int(d)<16):
    r=int(d)+55
    print(chr(r))
    
