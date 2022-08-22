##18.write a python program on characterscounter
## 
##Note the following points: 
##1.	The method should scan the given input, and count the number of times the given character “toFind” occurs in the input string. Return the number of times the given character occurs in
##the input string. 
##2.	If input is null or empty, return -1. 
##3.	Example input: “Hello World”, and 'H”, you must return 1, since 'H' occurs once in “Hello World”. 
##4.	The character must be searched for regardless of case. If upper case H is given as the character to find, the method must search for lower and uppercase 'H' and return the number of times
##it exists.

a=input()
b=input()
for i in a:
    x=a.count(b)
if b in " ":
    print("-1")
else:
    print(x)
     
