'''
def generator():
    yield 1+2
    yield 3
for i in generator():
    print(i)
'''
##===================================================================
'''
def generator():
    yield 1*2
    yield 2*3
x=generator()
print(x.__next__())
print(x.__next__())
print(x.__next__())
'''
##=======================================================================
'''
def square():
    i=1
    while True:
        yield i*i
        i+=1
for val in square():
    if val>10:
        break
    print(val)
'''
##=========================================================================
'''
def fib(x):
    a,b=0,1
    while a<x:
        yield a
        a,b=b,a+b
p=fib(5)
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
for i in p:
    print(i)
'''
##===========================================================================
'''
exp=(i**2 for i in range(10))
for i in exp:
    print(i)
'''
##============================================================================
'''
def acc():
    b=0
    c=None
    while True:
        c=yield b
        if c is None:
            break
        b+=c
generator=acc()
next(generator)
print(generator.send(1))
print(generator.send(10))
print(generator.send(100))
'''
##===========================================================================

