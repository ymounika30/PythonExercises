##13.Write a program that accepts a sentence and calculate the number of letters and digits.
##Suppose the following input is supplied to the program:
##hello world! 123
##Then, the output should be:
##LETTERS 10
##DIGITS 3
a=input()
b=0
c=0
for i in a:
    if i.isdigit():
        b=b+1
    elif i.isalpha():
        c=c+1
print("LETTERS " +str(c))
print("DIGITS " +str(b))
    
