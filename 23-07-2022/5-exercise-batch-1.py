##1.Write a Python program to get all possible combinations of the elements of a given list using itertools module.
'''
import itertools
def combination(l1):
    b=[]
    for i in range(len(l1)+1):
        b.append(list(itertools.combinations(l1,i)))
    return b
a=[1,2,3,4]
print(combination(a))
'''
##==================================================================================================================================
##2.Write a python program to create an iterator that returns consecutive keys and groups from an iterable
'''
import itertools
a="MMMOOOOOUUUNNNNNIIIIIIKKKKKKKKKKKAAAAAAAA"
x=itertools.groupby(a)
for i,j in x:
    print(i)
    print(list(j))
'''
##====================================================================================================================================
##3. Write a Python program to find the years where 25th of December be a Sunday between 2000 and 2150.
from datetime import date
def Years():
    for i in range(2000,2151):
        def isSunday(i):
            return 6==date(i,12,25).weekday()
        if isSunday(i):
            print(i)
Years()
                                   

##=====================================================================================================================================
##4.write a python program using generator write armstrong.
'''
def armstrong(a):
    n=len(a)
    b=0
    for i in a:
        x=int(i)
        b=b+(x**n)
    yield b
a=input()
print(list(armstrong(a)))
'''
##======================================================================================================================================
##5.write a python program by using math module use 3 function for each function one example.
'''
import math
print(math.tau)
print(math.pi)
print(math.e)
'''
