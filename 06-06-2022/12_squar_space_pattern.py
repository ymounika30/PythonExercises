##12.Write a program to print the following Pattern
##    * * * * * 
##    *       * 
##    *       * 
##    *       * 
##    * * * * * 
a=int(input())
print("* "*a)
for i in range(2,a+1):
    print("* "+(a-2)*"  "+"*")
print("* "*a)
