#SingleInheritanceExample
class Father:            #Parent class
    money=1000
    def display(self):
        print("Parent class Instance method")
    @classmethod
    def display_money(cls):
        print("Parent Class classmethod:", cls.money)
    @staticmethod
    def stat():
        a=10
        print("Parent Class Static Method: ",a)
class Son(Father):
    def disp(self):
        print("Child class Instance Method")
s=Son()
s.disp()
s.display()
s.display_money()
s.stat()
