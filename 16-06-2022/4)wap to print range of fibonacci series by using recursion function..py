#4)wap to print range of fibonacci series by using recursion function.'''
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of number"))
for i in range(n):
 print(fibonacci(i))
