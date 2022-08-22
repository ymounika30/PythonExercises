##import sys
##number=1
##
##if len(sys.argv)==2:
##    number=int(sys.argv[1])
##
##for i in range(number):
##    print("Rakesh Kumar Sahoo")

##import sys
##sys.path

"""ISINSTANCE """
##class Myclass:
##    def __init__(self,name):
##        self.name=name
##
##    def details(self):
##        print("My Name is {}".format(self.name))
##
##m=Myclass("Rakesh")
##m.details()
##
##x=isinstance(m,Myclass)
##print(x)
"""ISSUBCLASS"""

##class Teacher(object):
##    def __init__(self):
##        print("I am from Parent class Constructor.")
##        
##    def disp(self):
##        print("I am a Techer class Method.")
##
##class Student(Teacher):
##    def __init__(self):
##        print("I am from Child Class Constructor")
##    def disp_1(self):
##        print("I am Student class Method.")
##
##s=Student()
##s.disp_1()
##
##x=issubclass(Student,Teacher)
##print(x)

##class Employee(object):
##    def set_name(self,name):
##        self.name=name
##        
##
##    def get_name(self):
##        print("My Name Is :",self.name)
##
##
##
##e=Employee()
##
##e.set_name("Rakesh")
##e.get_name()
""" Setter And Getter Method"""

##
##class Friend:
##    def __init__(self,job):
##        self.job = job
##
##    def getJob(self):
##        return self.job
##
##    def setJob(self, job):
##        self.job = job


##Bob = Friend("Painting")
##print(Bob.getJob())
##Bob.setJob("Builder")
##print(Bob.getJob())
##
##ob=Friend("Pilot")
##print(ob.getJob())
##ob.setJob("LocoPilot")
##print(ob.getJob())
