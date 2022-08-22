##Python Program to Find the Factors of a Number 
a=int(input())
for i in range(1,a+1):
    if (a%i)==0:
        print(i)
