##12.  Write a python program StarPattern, which accepts a number as command line argument and prints the following output: 
##Input: 4 
##Output: 
##*  
##*  *  
##*  *  *  
##*  *  *  * 
##NOTE: Output stars must also be separated by a single space. The number of lines must equal the number passed as argument. Negative numbers or zero should print “Error” and exit. Numbers up to 10 must be handled. 
a=int(input())
for i in range(1,a+1):
    print("* "*i)


##Input: 4 
##Output: 
##*  
##*  *  
##*  *  *  
##*  *  *  * 
