##3.Write a program to print the following Pattern
##  5 5 5 5 5 
##  4 4 4 4 4 
##  3 3 3 3 3 
##  2 2 2 2 2 
##  1 1 1 1 1
a=int(input())
for i in range(a):
    for j in range(1,a+1):
        print(a-i,end=" ")
    print()
