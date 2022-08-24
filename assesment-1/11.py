##11. Write a python  program Box, which accepts 2 numbers as command line argument and prints the following output: 
##Input: 4 5 
##Output: 
## *  *  *  *  * 
## *              * 
## *              * 
## *  *  *  *  * 
##NOTE: Output stars must also be separated by a single space. The first argument is the number of rows and the second argument is the number of columns. Negative numbers or 0 should print “Error” and come out. Numbers up to 30 must be handled. 
a=int(input())
b=int(input())
print("* "*b)
for i in range(a-2):
    star="* "+"  "*(a-1)+"*"
    print(star)
print("* "*b)
      


##Input: 4 5 
##Output: 
## *  *  *  *  * 
## *               * 
## *               * 
## *  *  *  *  *
