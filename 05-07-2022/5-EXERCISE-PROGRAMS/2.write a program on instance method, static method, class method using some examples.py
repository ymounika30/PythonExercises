##2.write a program on instance method, static method, class method using some examples
##instancemethod
'''
class Shape:
    def __init__(self,edge,color):
        self.edge=edge
        self.color=color
    def find_edges(self):
        return self.edge
    def modify_edges(self,newedge):
        self.edge=newedge
circle=Shape(0, "red")
square=Shape(4, "blue")
print("No of edges for square: ",str(circle.find_edges()))
square.modify_edges(6)
print("No of edges for square: ",str(square.find_edges()))
'''

##class method
'''
from datetime import date
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_birth_year(cls,name,year):
        return cls(name,date.today().year-year)
person1=Person("Mounika",25)
person2=Person.from_birth_year("Mounika",1994)
print(person1.age)
print(person2.age)
'''

##static method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def is_adult(age):
        return age>18
print(Person.is_adult(22))

