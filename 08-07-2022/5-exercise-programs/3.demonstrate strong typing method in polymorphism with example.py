##3.demonstrate strong typing method in polymorphism with example
class Duck:
    def walk(self):
        print("thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak")
class Cat:
    def talk(self):
        print("Meow Meow")
def fun(obj):
    if hasattr(obj, 'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
d=Duck()
fun(d)

h=Horse()
fun(h)

c=Cat()
fun(c)
