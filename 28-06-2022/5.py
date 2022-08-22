##5.write a python program  to print the number from a given number N till 0 using recursion.
n = int(input("enter the number:"))
def rec(n):
    if n==0:
        print(0)
    else:
        print(n)
        rec(n-1)
rec(n)
