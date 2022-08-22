##Python Program to Print the Fibonacci sequence 
def fibonacci(a):
    if a<=1:
        return a
    else:
        msg=fibonacci(a-1)+fibonacci(a-2)
    return msg
def fibonacci_series(a):
    list_a=[]
    for i in range(a):
        list_a+=[fibonacci(i)]
    return list_a
a=int(input())
x=fibonacci_series(a)
print(x)
