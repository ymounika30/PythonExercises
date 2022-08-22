##13. Write a python program NumberPattern4, which accepts a number as command line argument and prints the following output: 
##Input: 5 
##Output: 
##1 
##2 4 
##3 6 9 
##4 8 12 16 
##5 10 15 20 25 
## 
##NOTE: Output numbers must be separated by a single space. The number of lines must equal the number passed as argument. Negative numbers or zero as input should print “Error” and exit. Numbers up to 10 must be handled. 
##
a=int(input())
b=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
        b=b+1
    print()


##Input:5
##Output:
##1 
##2 4 
##3 6 9 
##4 8 12 16 
##5 10 15 20 25
