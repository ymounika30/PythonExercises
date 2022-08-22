##8.Write a program to print the following Pattern
##  1 
##  2 3 
##  3 4 5 
##  4 5 6 7 
##  5 6 7 8 9 
a=int(input())
for i in range(6):
    for j in range(i):
        print(i,end=" ")
        i=i+1
    print()
