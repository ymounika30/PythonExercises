##1). wap take one example duck typing,in this methods you must take 3 defferent classes names and in each one class you must take 3 defferent methods
class Duck:
    def walk(self):
        print("Quack Quack")
class Cat:
    def talk(self):
        pritn("Meow Meow")
class Dog:
    def shake(self):
        print("Bow Bow")
def fun(obj):
    obj.talk()
d=Duck()
d1=Dog()
c=Cat()
fun(d)
fun(d1)
fun(c)
    
