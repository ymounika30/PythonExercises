##5.Write a program to print the following Pattern
##  1 
##  2 2 
##  3 3 3 
##  4 4 4 4 
##  5 5 5 5 5
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")
