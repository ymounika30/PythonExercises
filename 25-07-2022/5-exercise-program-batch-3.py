##1) wap to create class and create two objects from that class and add those two objects using _add_ (operator overloading)
'''
class Add:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
add1=Add(1)
add2=Add(2)
print(add1+add2)
'''
##=================================================================================================================================================
##2)wap to create a generator by using send method
'''
def generator(a):
    num=yield
    while num<a:
        num=yield num
        num+=1
n=generator(20)
next(n)
print(n.send(10))
'''
##=================================================================================================================================================
##3) wap to create the generator comprehension
'''
x=(i for i in range(10) if i%2==0)
for i in x:
    print(i,end=" ")
'''
##==================================================================================================================================================
##4) print a function n number of times using decorator
'''
def fun1(func):
    def fun2(a):
        return func(a)
    return fun2
@fun1
def div(a):
    for i in range(a):
        print("hello")
  
div(a=int(input("enter a number: ")))    
'''
##==================================================================================================================================================
##5) write a python program to check the how many instance variables are there in a class.
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self,course):
        self.course=course
s=Student("Mounika",25)
s.display("python")
print("total instance variables ={}".format(s.__dict__))
print("no of instance variables={}".format(len(s.__dict__)))
'''
