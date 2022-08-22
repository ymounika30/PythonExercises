##5.Create a Student class and then test the displayStudent method.
class Student:
    def __init__(self,name,id,grade):
        self.name=name
        self.id=id
        self.grade=grade
    def display_method(self):
        print("My name is: ",self.name)
        print("My age is: ",self.id)
        print("My grade is: ",self.grade)
s=Student(name=input(),id=int(input()),grade=input())
s.display_method()
