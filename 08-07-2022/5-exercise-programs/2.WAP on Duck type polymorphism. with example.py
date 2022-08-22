##2.WAP on Duck type polymorphism. with example
class Duck:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        print("Quack Quack")
class Car:
    def __init__(self,model):
        self.model=model
    def make_sound(self):
        print("I can make sound")

    
donald=Duck("Donald Duck",5)
car=Car("Innova")

def fun(obj):
    obj.make_sound()

fun(donald)
fun(car)
