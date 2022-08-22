'''1. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.'''
##def bold(a):
##    def wrapped():
##        return "<b>"+a()+"</b>"
##    return wrapped
##def italic(a):
##    def wrapped():
##        return "<i>"+a()+"</i>"
##    return wrapped
##def underline(a):
##    def wrapped():
##        return "<u>"+a()+"</u>"
##    return wrapped
##@bold
##@italic
##@underline
##def new():
##    return "Hello World"
##print(new())
##===========================================================================================================================
'''2. Write a Python program to extract specified size of strings from a give list of string values using lambda
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']'''
##def extract_string(a,n):
##    res=list(filter(lambda e:len(e)==n,a))
##    return res
##a=['Python', 'list', 'exercises', 'practice', 'solution']
##n=8
##print(extract_string(a,n))
    
##===========================================================================================================================
'''3. Write a Python program to create a deep copy of a given dictionary. Use copy.copy'''
##import copy
##student={
##    "name":"Mounika",
##    "id":22114,
##    "course":"python"
##    }
##colleage=copy.copy(student)
##print(colleage)

##===========================================================================================================================
'''4. Write a Python Program to Check a Number is a Spy Number or Not? note:- without  forloop.'''
##a=int(input())
##b=0
##p=1
##while a>0:
##    d=a%10
##    b=b+d
##    p=p*d
##    a=a//10
##if b==p:
##    print("Spy number")
##else:
##    print("Not a spy number")
##===========================================================================================================================
'''5. Write a Python program to find the XOR of two given strings interpreted as binary numbers.
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111'''
##def binary_numbers(a):
##    return bin(int(a[0],2) ^ int(a[1],2))
##a=["0001","1011"]
##print(binary_numbers(a))
