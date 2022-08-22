##7.Write a program to print the following Pattern
##  5 
##  4 4 
##  3 3 3 
##  2 2 2 2 
##  1 1 1 1 1
a=6
for i in range(6):
    for j in range(i):
        print(a,end=" ")
    a-=1
    print(" ")
