##5) Write a Python Program for Even Number Pyramid Pattern
a=int(input())
x=2
for i in range(1,a+1):
    s=""
    start_spaces=((a-i)*" ")
    for i in range(1,i+1):
        s=s+str(x)+" "
        x=x+2
    print(start_spaces+s)
