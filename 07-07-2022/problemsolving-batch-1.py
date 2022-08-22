##1.Define a class named Shape and its subclass Square.
##The Square class has an init function which takes a length as argument.
##Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
##
##Hints:
##
##To override a method in super class, we can define a method with the same name in the super class.
class Shape:
    def __init__(self,length):
        self.length=length
    def area(self):
        area=0
class Square(Shape):
    def __init__(self,length):
        super().__init__(length)
        self.length=length
    def area(self):
        area=self.length*self.length
        print("Area is:", area)
length=int(input())
area=Square(length)
area.area()
        
