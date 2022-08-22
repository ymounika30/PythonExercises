##Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff
class Staff:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Role: ",self.role)
        print("Department: ",self.dept)
        print("Salary: ",self.salary)
class Teacher(Staff):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Teacher","Science",25000)
teacher=Teacher("Mounika",25)
teacher.display()
