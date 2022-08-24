##8. Write a python program EvenOrOdd, which accepts a whole number as command line argument and prints “Even Number”
##if the number is Even and prints “Odd Number” if the number is Odd. If the input is not a number, print “Error”. 
a=input()
x=int(a)
if (x%2)==0:
    print("Even")
elif (x%2)!=0:
    print("Odd")
else:
    print("Error")

##Input:22
##Ouput:Even
##Input:31
##Output:Odd

