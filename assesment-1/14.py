##14. Write a python  program on Prime numbers
a=int(input())
f=0
for i in range(2,a):
    if (a%i)==0:
        f=f+1
if f==0:
    print("Prime Numbers")
else:
    print("Not a Prime Numbers")
    

##Input:7
##Output:Prime Numbers
