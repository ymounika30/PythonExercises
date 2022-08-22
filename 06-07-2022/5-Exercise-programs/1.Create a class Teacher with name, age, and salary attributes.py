##1.Create a class Teacher with name, age, and salary attributes,
##where salary must be a private attribute that cannot be accessed outside the class.
class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print("My name is: ",self.name)
        print("My age is: ",self.age)
        print("My salary is: ",self.salary)
t=Teacher(name=input(),age=int(input()),salary=int(input()))
t.display()
