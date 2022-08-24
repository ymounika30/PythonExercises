##10. Write a python program DigitChecker, which accepts a two digit number as command line argument and prints Zero if the digits are same and if the two digits are different,
##it prints their difference. 
##Ex: Input: 52 
##Output: 3 
##Input: 88 
##Output: 0 
## 
##Note: Please do not use Conditional or Looping statements to solve the given problem
a=int(input())
a=str(a)
num_1=int(a[0])
num_2=int(a[1])
if(num_1==num_2):
    print("0")
else:
    print(num_1-num_2)



##Input: 52 
##Output: 3 
##Input: 88 
##Output: 0 
