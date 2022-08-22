##4.write a python program using oops concepts find a fibonacci series
class Fib:
    def func(self,num):
        a=0
        b=1
        for i in range(num):
            c=a+b
            a=b
            b=c
            print(c)
obj=Fib()
obj.func(10)


