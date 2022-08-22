##Write a program that prints the class name using its object.
class Student:
    def name(self,name):
        return name
s1=Student()
print(type(s1).__name__)
