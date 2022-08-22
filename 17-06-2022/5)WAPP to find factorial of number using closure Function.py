#5)WAPP to find factorial of number using closure Function.'''

def factori():
    def fun(n):
        fact=1
        while n>0:
            fact=fact*n
            n=n-1
        return fact
n=int(input())
print(fun(n))
