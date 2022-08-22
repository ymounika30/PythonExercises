##16.Write a program to print the following Pattern
##	           1
##              3  2
##       6   5   4
##10  9   8   7
a=int(input())
x=1
for i in range(1,a+1):
    spaces=((a-i)*"  ")
    c=""
    for j in range(1,i+1):
        c=str(x)+"  "+c
        x+=1
    print(spaces+c)
