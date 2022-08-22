##4).wap  take one eaxmple in hierarchical method
class Father:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("Name ",self.name)
        print("Age ",self.age)
class Daughter(Father):
    def __init__(self,name,age,surname):
        super().__init__(name,age)
        self.surname=surname
    def disp1(self):
        print("Surname ",self.surname)
class Son(Father):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender
    def disp2(self):
        print("Gender ",self.gender)
s=Son("Apparao",52,"Male")
d=Daughter("Apparao",52,"Yarramasa")
s.disp()
s.disp2()
d.disp()
d.disp1()
