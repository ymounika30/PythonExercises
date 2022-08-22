##12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
##The numbers obtained should be printed in a comma-separated sequence on a single line.
a=int(input())
b=int(input())
for i in range(a,b+1):
    if (i%2)==0:
        print(i, end=",")
