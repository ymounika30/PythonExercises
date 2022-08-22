##3.Python Program to Find HCF or GCD
'''a=int(input())
b=int(input())
if a>b:
    small=a
else:
    small=b
for i in range(1,small+1):
    if((a%i)==0)and((b%i)==0):
        x=i
print(x)
'''
a=int(input())
b=int(input())
if a>b:
    great=a
else:
    great=b
lcm=False
for i in range(great,(a*b+1)):
    if not lcm:
        if(i%a)==0 and (i%b)==0:
            lcm=True
            great=i
gcd=a*b//great
print(gcd)
