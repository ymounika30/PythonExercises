##1.write a program Example 9: Pascal's Triangle
##           1
##         1   1
##       1   2   1
##     1   3   3    1
##   1  4    6   4   1
## 1  5   10   10  5   1
from math import factorial
a=int(input())
for i in range(1,a+1):
    for j in range(a-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()

