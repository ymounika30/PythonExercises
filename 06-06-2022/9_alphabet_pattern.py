##9.Write a program to print the following Pattern
##  A 
##  B C
##  D E F
##  G H I J
##  K L M N O
a=int(input())
b=65
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(b),end=" ")
        b=b+1
    print()
