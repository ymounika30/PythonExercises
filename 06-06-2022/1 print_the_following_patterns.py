##1. Write a program to print the following Patterns
##  1 2 3 4 5 
##  1 2 3 4 5  
##  1 2 3 4 5 
##  1 2 3 4 5 
##  1 2 3 4 5
a=int(input())
for i in range(a):
    for j in range(a):
        print(j+1,end=" ")
    print(" ")
