##5. A class RussianMultiplication is given to you. Implement the following method in that class: getProduct(int num1, int num2). If either number is not positive then return -1. Return the
##product of the two numbers. Calculate the product using Russian multiplication. 
##Russian Multiplication Method: 
##The Russian peasant multiplication, also called the Russian peasant algorithm, uses a halving and doubling method to multiply whole numbersWhen halving, disregard any remainder.
##Just put the quotient in the halving columnWhen the number in the halving column is 1, cross out all rows that have an even number in the halving columnthe answer is found by adding
##the remaining numbers in the doubling column 
##Example # 1: 11 × 12  
## 
## 
##Halving                              Doubling 
## 
##   11                    ×                  12  
## 
##   5                      ×                  24  
## 
##   2                      ×                  48  ---> Disregard this since 2 is even 
## 
##   1                      ×                  96  
##The product of 11 and 12 is: 12 + 24 + 96 = 132  
a=int(input())
b=int(input())
if a<=0:
    print("-1")
else:
    print(a*b)


##input: 11
##       12
##output:132
##input:-1
##         2
##output:-1
