##2.write demo programs for method overriding,constructor overriding,program with variable number of arguments.
#method overriding
class Parent:
    def __init__(self):
        self.value="Inside Parent"
    def show(self):
        print(self.value)
class Child(Parent):
    def __init__(self):
        self.value="Inside Child"
    def show(self):
        print(self.value)

c=Child()
p=Parent()
p.show()
c.show()

print("=======================================================")

##constructor overriding
class Father:
    def __init__(self):
        money=1000
        print("Father class constructor")
    def display(self):
        print("Father Class Instance Method")
class Son(Father):
    def __init__(self):
        self.money=1000
        self.car="BMW"
        print("Son Class Constructor")
    def disp(self):
        print("Son Class Instance Method")
s=Son()
print(s.money)
print(s.car)
s.disp()
s.display()

print("==============================================")

#program with variable number of arguments
class A:
    def sum(self,*a):
        for x in a:
            print(x)
s=A()
s.sum()
s.sum(10)
s.sum(10,20)
s.sum(10,20,30)

