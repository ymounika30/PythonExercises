##17.Write a program to print the following Pattern
##10  9  8   7
##      6   5  4
##           3  2
##               1
## 
a=10
for i in range(4):#rows
    space="  "*i
    print(space,end=" ")
    for j in range(4-i):
        print(a,end=" ")
        a=a-1
    print()
