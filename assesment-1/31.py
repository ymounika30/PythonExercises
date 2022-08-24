##31. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.  
##Sample Output:
##Double the number of 15 = 30
##Triple the number of 15 = 45
##Quadruple the number of 15 = 60
##Quintuple the number 15 = 75
def num(a):
    for i in range(1,10):
        x=(a*i)
        print(a," = ",x)
a=int(input())
num(a)

##Input: 15
##Output:
##15  =  15
##15  =  30
##15  =  45
##15  =  60
##15  =  75
##15  =  90
##15  =  105
##15  =  120
##15  =  135
