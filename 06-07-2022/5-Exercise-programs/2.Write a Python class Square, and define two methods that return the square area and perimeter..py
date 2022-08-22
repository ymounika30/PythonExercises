##2.Write a Python class Square, and define two methods that return the square area and perimeter.
class Square:
    def __init__(self,a):
        self.a=a
    def area(self):
        print(self.a*self.a)
    def perimeter(self):
        print(self.a*4)
s=Square(a=int(input()))
s.area()
s.perimeter()
