##Python Program to Find LCM 
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
print(great)
