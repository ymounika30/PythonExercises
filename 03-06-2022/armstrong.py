a=input()
b=0
n=len(a)
for i in a:
    x=int(i)
    b=b+(x**n)
a=int(a)
if b==a:
    print("True")
else:
    print("False")
    
    
