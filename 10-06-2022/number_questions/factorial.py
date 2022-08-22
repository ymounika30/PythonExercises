##Python Program to Find the Factorial of a Number 
def factorial(a):
    if a==1:
        return a
    else:
        return a*factorial(a-1)
a=int(input())
x=factorial(a)
print(x)
