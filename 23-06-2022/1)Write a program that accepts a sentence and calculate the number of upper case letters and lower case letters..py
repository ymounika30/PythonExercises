##1)Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
##Suppose the following input is supplied to the program:
##Hello world!
##Then, the output should be:
##UPPER CASE 1
##LOWER CASE 9
a=input()
b=0
c=0
for i in a:
    if i.isupper():
        b=b+1
    elif i.islower():
        c=c+1
print(b)
print(c)
