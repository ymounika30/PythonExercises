##10.Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle:
    def __init__(self,a,b):
        self.length=a
        self.breadth=b
    def rectangle_area(self):
        return self.length*self.breadth
new_rectangle=Rectangle(3,4)
print(new_rectangle.rectangle_area())
