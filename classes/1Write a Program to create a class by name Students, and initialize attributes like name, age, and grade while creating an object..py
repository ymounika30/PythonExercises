##Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My grade is:",self.grade)
s1=Student("Mounika",25,"A")
s2=Student("Laxmi",45,"B")
s1.display()
s2.display()
        
