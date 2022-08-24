#Single Inheritance with Constructor Inheritance
class Father:
    def __init__(self):
        self.money=1000
        print("Father class constructor")
    def display(self):
        print("Father class Instance method")
class Son(Father):
    def disp(self):
        print("Son class Instance method", self.money)
s=Son()
s.disp()
print("Instance Variable: ",s.money)
s.display()
