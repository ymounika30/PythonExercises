##6.a. Write a Python function that takes a number as a parameter and check the number is prime or not. 

'''
def prime(a):
    for i in range(1,a+1):
        f=0
        for j in range(2,i):
            if (i%j)==0:
                f=f+1
    if f==0:
        print("Prime")
    else:
        print("Not a Prime")
a=int(input())
prime(a)
'''
##Output:
##4
##Not a Prime
##3
##Prime

##==================================================================================================================================================

##b. Write a Python function that checks whether a passed number is palindrome or not
def palindrome(a):
    if a[::-1]==a:
        print("Palindrome")
    else:
        print("Not a Palindrome")
a=input()
palindrome(a)

##Output
##123
##Not a Palindrome
##121
##Palindrome
