##1.write a python program to find the Nth term in a fibonacci series using recursion.
def fibonacci(a):
    if a<=1:
        return a
    else:
        msg=fibonacci(a-2)+fibonacci(a-1)
    return msg
a=int(input())
print(fibonacci(a))
