##3.How to copy all properties of an object to another object in Python?
class Student:
    def __init__(self):
        super(Student).__init__()
        self.a=1
        self.b=2
obj1=Student()
obj2=Student()
obj1.a=int(input())
obj2.__dict__.update(obj1.__dict__)
print(obj1.a)
print(obj2.a)
