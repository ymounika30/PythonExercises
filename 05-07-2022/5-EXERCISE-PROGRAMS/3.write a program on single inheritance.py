##3.write a program on single inheritance
class Parent:
    def func1(self):
        print("The function is in parent class")
class Child(Parent):
    def func2(self):
        print("The function is in child class")
object1=Child()
object1.func1()
object1.func2()
        
