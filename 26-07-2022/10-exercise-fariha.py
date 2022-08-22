##1.write a python program in prime number using outer and inner function
'''
def outer(a):
    def inner(x):
        f=0
        x=int(input())
        for i in range(2,x):
            if (x%i)==0:
                f=f+1
        if f==0:
            print("Prime")
        else:
            print("Not a Prime")
    return inner
def new(x):
    pass
res=outer(new)
res(5)
'''
##1.write a python program in prime number using decorator
'''
def outer(a):
    def inner():
        x=int(input())
        f=0
        for i in range(2,x):
            if (x%i)==0:
                f=f+1
        if f==0:
            print("Prime")
        else:
            print("Not a Prime")
    return inner
@outer
def new():
    pass
new()
'''
##1.write a python program in prime number using sys module
'''
from sys import argv
a=int(argv[1])
f=0
for i in range(2,a):
    if (a%i)==0:
        f=f+1
if f==0:
    print("Prime")
else:
    print("Not a Prime")
'''
##==============================================================================================================================================================
##2.write a python program in armstrong number using outer and inner function
'''
def outer(a):
    def inner():
        p=int(input())
        n=len(str(p))
        b=0
        x=p
        while(x>0):
            c=x%10
            b=b+c**n
            x=x//10
        if p==b:
            print("Armstrong")
        else:
            print("Not a Armstrong")
    return inner
def new():
    pass
res=outer(new)
res()
'''
##2.write a python program in armstrong number using decorator
'''
def outer(a):
    def inner():
        p=int(input())
        n=len(str(p))
        b=0
        x=p
        while(x>0):
            c=x%10
            b=b+c**n
            x=x//10
        if p==b:
            print("Armstrong")
        else:
            print("Not a Armstrong")
    return inner
@outer
def new():
    pass
new()
'''
##2.write a python program in armstrong number using sys module
'''
from sys import argv
a=int(argv[1])
b=0
n=len(str(a))
x=a
while x>0:
    r=x%10
    b=b+(r**n)
    x=x//10
if a==b:
    print("Armstrong")
else:
    print("Not a Armstrong")
'''    
##=================================================================================================================================================================
##3.write a python program in strong number using outer and inner function
'''
def outer(a):
    def inner():
        b=0
        x=int(input())
        n=x
        while(x):
            i=1
            fact=1
            rem=x%10
            while (i<=rem):
                fact=fact*i
                i=i+1
            b=b+fact
            x=x//10
        if b==n:
            print("Strong Number")
        else:
            ptint("Not a Armstrong")
    return inner
def new():
    pass
res=outer(new)
res()
'''
##3.write a python program in strong number using decorator
'''
def outer(a):
    def inner():
        b=0
        x=int(input())
        n=x
        while(x):
            i=1
            fact=1
            rem=x%10
            while (i<=rem):
                fact=fact*i
                i=i+1
            b=b+fact
            x=x//10
        if b==n:
            print("Strong Number")
        else:
            ptint("Not a Armstrong")
    return inner
@outer
def new():
    pass
new()
'''
##3.write a python program in strong number using sys module
'''
from sys import argv
a=int(argv[1])
b=0
n=a
while(a):
    i=1
    fact=1
    rem=a%10
    while(i<=rem):
        fact=fact*i
        i=i+1
    b=b+fact
    a=a//10
if b==n:
    print("Strong Number")
else:
    print("Not a Strong Number")
'''
##===================================================================================================================================================================
##4.write a python program in palindrome for integers using inner and outer function
'''
def outer(a):
    def inner():
        x=int(input())
        n=x
        b=0
        while x>0:
            dig=x%10
            b=b*10+dig
            x=x//10
        if n==b:
            print("Palindrome")
        else:
            print("Not a Palindrome")
    return inner
def new():
    pass
res=outer(new)
res()
'''
##4.write a python program in palindrome for integers using decorators
'''
def outer(a):
    def inner():
        x=int(input())
        n=x
        b=0
        while x>0:
            dig=x%10
            b=b*10+dig
            x=x//10
        if n==b:
            print("Palindrome")
        else:
            print("Not a Palindrome")
    return inner
@outer
def new():
    pass
new()
'''
##4.write a python program in palindrome for integers using sys module
'''
from sys import argv
a=int(argv[1])
b=0
n=a
while a>0:
    dig=a%10
    b=b*10+dig
    a=a//10
if b==n:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
##=====================================================================================================

##5.write a python program in perfect number using outer and inner function
'''
def outer(a):
    def inner():
        x=int(input())
        b=0
        for i in range(1,x):
            if(x%i)==0:
                b=b+i
        if b==x:
            print("Perfect Number")
        else:
            print("Not a Perfect Number")
    return inner
def new():
    pass
res=outer(new)
res()
'''
##5.write a python program in perfect number using decorators
'''
def outer(a):
    def inner():
        x=int(input())
        b=0
        for i in range(1,x):
            if(x%i)==0:
                b=b+i
        if b==x:
            print("Perfect Number")
        else:
            print("Not a Perfect Number")
    return inner
@outer
def new():
    pass
new()
'''
##5.write a python program in perfect number using sys module
'''
from sys import argv
a=int(argv[1])
b=0
for i in range(1,a):
    if(a%i)==0:
        b=b+i
if b==a:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
'''
##=====================================================================================================

##6.write a python program in factorial number using outer and inner function
'''
def outer(a):
    def inner():
        x=int(input())
        fact=1
        for i in range(1,x+1):
            fact=fact*i
        print(fact)
    return inner
def new():
    pass
res=outer(new)
res()
'''
##6.write a python program in factorial number using decorators
'''
def outer(a):
    def inner():
        x=int(input())
        fact=1
        for i in range(1,x+1):
            fact=fact*i
        print(fact)
    return inner
@outer
def new():
    pass
new()
'''
##6.write a python program in factorial number using sys module
'''
from sys import argv
a=int(argv[1])
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
'''
##=====================================================================================================

##7.write a python program in odd or even number using outer and inner function
'''
def outer(a):
    def inner():
        x=int(input())
        if x%2==0:
            print("Even")
        else:
            print("Odd")
    return inner
def new():
    pass
res=outer(new)
res()
'''
##7.write a python program in odd or even number using decorators
'''
def outer(a):
    def inner():
        x=int(input())
        if x%2==0:
            print("Even")
        else:
            print("Odd")
    return inner

@outer
def new():
    pass
new()
'''
##7.write a python program in odd or even number using sys module
'''
from sys import argv
a=int(argv[1])
if a%2==0:
    print("Even")
else:
    print("Odd")
'''
##=====================================================================================================

##8.write a python program in positive or negative number using outer and inner function
'''
def outer(a):
    def inner():
        x=int(input())
        if x<0:
            print("Negative")
        elif x==0:
            print("Zero")
        else:
            print("Positive")
    return inner
def new():
    pass
res=outer(new)
res()
'''
##8.write a python program in positive or negative number using decorators
'''
def outer(a):
    def inner():
        x=int(input())
        if x<0:
            print("Negative")
        elif x==0:
            print("Zero")
        else:
            print("Positive")
    return inner
@outer
def new():
    pass
new()
'''
##8.write a python program in positive or negative number using sys module
'''
from sys import argv
a=int(argv[1])
if a<0:
    print("Negative")
elif a==0:
    print("Zero")
else:
    print("Positive")
'''    
##================================================================================================
##9.write a python program convert octal to decimal  using outer and inner function
'''
def outer(a):
    def inner():
        n=int(input())
        sum=0
        i=1
        while(n):
            c=n%10
            n=n//10
            sum=sum+c*i
            i=i*8
        print(sum)
    return inner
def new():
    pass
res=outer(new)
res()
'''
##9.write a python program convert octal to decimal  using decorators
'''
def outer(a):
    def inner():
        n=int(input())
        sum=0
        i=1
        while(n):
            c=n%10
            n=n//10
            sum=sum+c*i
            i=i*8
        print(sum)
    return inner
@outer
def new():
    pass
new()
'''
##9.write a python program convert octal to decimal  using sys module
'''
from sys import argv
a=int(argv[1])
b=0
i=1
while(a):
    c=a%10
    a=a//10
    b=b+c*i
    i=i*8
print(b)
'''
##==================================================================================

##10.write a python program in lcm number using outer and inner function 
'''
def outer(x):
    def inner():
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
        if great==a:
            print("a is great")
        else:
            print("b is great")
    return inner
def new():
    pass
res=outer(new)
res()
'''
##10.write a python program in lcm number using decorators
'''
def outer(x):
    def inner():
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
        if great==a:
            print("a is great")
        else:
            print("b is great")
    return inner
@outer
def new():
    pass
new()
'''
##10.write a python program in lcm number using sys module
'''
from sys import argv
a=int(argv[1])
b=int(argv[2])
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
if great==a:
    print("a is great")
else:
    print("b is great")
'''
