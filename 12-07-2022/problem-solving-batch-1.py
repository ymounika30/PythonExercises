'''Write Program  to calculate area of different Figures such as circle,rectangle and square by 
using method overriding and implementing polymorphism.'''

class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        A=3.14*self.r*self.r
        print(A)
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        print(self.l*self.w)
class Square:
    def __init__(self,a):
        self.a=a
    def area(self):
        print(self.a*self.a)


print("Area of circle")
c=Circle(23)
c.area()
print("--------Area of Rectangle--------")
r=Rectangle(l=3,w=5)
r.area()
print("---------Area of square----------")
s=Square(a=5)
s.area()
