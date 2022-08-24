##Write a Python program that checks if one class is a subclass of another?
class Parent:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Child(Parent):
    def __init__(self,name,id,car):
        self.car=car
        super().__init__(name,id)
    def det(self):
        print("this is",self.name,"id is ",self.id,"brand",self.car)
s1=Child("Mounika",22114,"innova")
s1.det()
