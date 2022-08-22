##4) write a program to print a program like below
##
##          1   
##        1   1
##      1   2   1
##    1   3   3   1
##  1   4   4   4   1
##1   5   5   5   5   1
a=int(input())
s=""
print((a*" ")+"1")
print(((a-1)*" ")+"1"+" "+"1")
for i in range(2,a+1):
    start=((a-i)*" ")
    nums=(" "+str(i)+" ")*(i-1)
    s=start+"1 "+nums+"1 "
    print(s)
