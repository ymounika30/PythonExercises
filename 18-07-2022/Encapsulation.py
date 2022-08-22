# program to illustrate public access modifier in a class

"""Public"""
##class Student(object):
##    def __init__(self,id,name):
##        self.id=id
##        self.name=name
##
##
##    def details(self):
##        print("Name:",self.name)
##
##
##
##ob=Student(22069,"Rakesh")
##ob.details()

"""Protected Attributes->Protected attributes can accessible whereever in the class and inside the child class only."""

##class Employee(object):
##    def __init__(self,name,job):
##        self._name=name
##        self._job=job
##
##    def details_Employee(self):
##        print("My Name is {} and I am a {}.".format(self._name, self._job))
##
##e=Employee("Mounika","Java Devloper")
##e.details_Employee()

"""Private Attributes-> We cant acces private attribute outside the class directly we can acccess only inside the class.
But indirectly we can access the private attributes"""

##class Student(object):
##    def __init__(self,name,project):
##        self.name=name
##        self.__project=project
##
##    def student_Details(self):
##        print("Project:",self.__project)
##
##
##
##s=Student("Mounika","BLOGGING")
##
##s.student_Details()
##

"""Accessing at outside  the class."""
##Syntax->object._classname__variablename

##class Test:
##    def __init__(self):
##        self.__x=10
##
##t=Test()
##print(t._Test__x)
