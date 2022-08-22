##1.Define Multiple inheritance and write an example?
class Father:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print("Name ",self.name)
class Mother:
    def __init__(self,surname):
        self.surname=surname
    def disp_1(self):
        print("Surname ",self.surname)
class Son(Father,Mother):
    def __init__(self,name,surname,middlename):
        Father.__init__(self,name)
        Mother.__init__(self,surname)
        self.middlename=middlename
    def disp_2(self):
        print("Middle Name ",self.middlename)
s=Son("Mounika","Yarramasa","Mouni")
s.disp()
s.disp_1()
s.disp_2()
