"""1.Write a Python function to check whether a string is a pangram or not. Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"]"""

##import string
##def ispangram(stri):
##    alphabet='abcdefghijklmnopqrstuvwxyz'
##    for i in alphabet:
##        if i not in stri.lower():
##            return False
##
##    return True
##print(ispangram("The quick brown fox jumps over the lazy dog"))
##

##==========================================================================================================================================

"""2.Write a program where the instance are deleted in one object will not be deleted from other object."""


##class Test:
##    def __del__(self):
##        print( "deleted")
##
##    def details(self):
##        print("Hello Guys:")
## 
##test = Test()
##t=Test()
##t.details()
##del test

##===========================================================

"""3.Write a Python program to make a chain of function decorators (bold, italic, underline etc.)."""

##def bold(string):
##    return "<b>"+string+"</b>"
##def italics(string):
##    return "<i>"+string+"</i>"
##def underline(string):
##    return "<u>"+string+"</u>"
##string="Tarak is a Good Boy."
##print(bold(string))
##print(italics(string))
##print(underline(string))

##==============================================================================================================================

"""4. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']"""

##list = ['p', 'q']
##n = 5
##list1 = ['{}{}'.format(x, y) for y in range(1, n+1) for x in list]
##print(list1)

##=======================================================================================================================================

"""5.Write a Python program to find missing and additional values in two lists."""
##a=[1,2,3,4]
##b=[3,4,5,6]
##print("Missing values in list1:",set(b).difference(set(a)))
##print("Missing values in list2:",set(a).difference(set(b)))
##print("additional values in list1:",set(a).difference(set(b)))
##print("additional values in list2:",set(b).difference(set(a)))




