##10.Write a program to check if elements of a list are same or not it read from front or back. E.g.-
##2	3	15	15	3	2
a=input()
b=[]
for i in a:
    b+=[i]
if b[::-1]==b:
    print("True")
else:
    print("False")
