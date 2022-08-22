##9. Write a python program Rounder, which accepts a whole number as command line argument and prints the same number if the input is Odd. If the input is even, it should print the next
##multiple of ten. If the input is not a number or is negative, print the string:“Error”. 
##Input: 44, output: 50 
##Input: 45, output: 45
a=int(input())
if(a%2)==0:
    print(a+(10-a)%10)
elif (a%2)!=0:
    print(a)


##Input:44
##Output:45
##Input:45
##Ouput:45

    

        
