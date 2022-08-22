##13.Write a program to print the following Pattern
##          * 
##        * * * 
##      * * * * * 
##    * * * * * * *
a=int(input())
for i in range(1,a+1):
    space=" "*(a-i)
    stars=""
    for j in range(1,i+1):
        stars=stars+("* "+" ")
    print(space+stars)
