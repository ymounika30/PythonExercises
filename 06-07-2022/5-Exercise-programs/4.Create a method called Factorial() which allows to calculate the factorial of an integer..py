##4.Create a method called Factorial() which allows to calculate the factorial of an integer.
##Test the method by instantiating the class.
class Factorial:
    def __init__(self,a):
        self.a=a
    def display(self):
        p=1
        if self.a<0:
            print("Factorial doesnot exist negative numbers")
        elif self.a==0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,self.a+1):
                p=p*i
            print(p)
f=Factorial(a=int(input()))
f.display()
            
            
