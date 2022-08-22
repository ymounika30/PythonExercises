##1.WAP to call parent class static static method from child class static method.
class Father:
    @staticmethod
    def static():
        a=10
        print("Father static method",a)
class Son(Father):
    @staticmethod
    def display():
        super(Son,Son).static()
s=Son()
s.static()
s.display()
    
