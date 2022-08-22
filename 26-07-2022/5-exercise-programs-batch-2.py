##1.. Write a Python program that invoke a given function after specific milliseconds. 
##inputs:100ms-16
##1000ms-100
##2000ms-25100
##Sample Output:
##Square root after specific miliseconds:
##4.0
##10.0
##158.42979517754858
'''
from time import sleep
import math
def delay(fn,milliseconds,*args):
    sleep(milliseconds/1000)
    return fn(*args)
print(delay(lambda a:math.sqrt(a),100,16))
print(delay(lambda a:math.sqrt(a),1000,100))
print(delay(lambda a:math.sqrt(a),2000,25100))
'''

##==================================================================================================================================================================================

##2.we will provide two lists list_1 and list_2.
##The list_1 and list_2 of this function represent the initial list. Need to comprehend by list:
##1Multiply each value in the two lists separately
##2Add each value in the two lists separately
##3Multiply the values in the two lists
##by using inner and outer functions 
'''
def outer(a):
    def inner():
        l1=[1,3,4,6,8]
        l2=[4,5,6,2,10]
        b=[]
        print(str(l1))
        print(str(l2))
        for i in range(0,len(l1)):
            b.append(l1[i]*l2[i])
        print(b)
    return inner
def new():
    pass
res=outer(new)
res()
'''
##===================================================================================================================================================================
##3.Write a Python program to build a list, using an iterator function and an initial seed value.
## 1.The iterator function accepts one argument (seed) and must always return a list with two elements ([value, nextSeed]) or False to terminate.
## 2.Use a generator function, fn_generator, that uses a while loop to call the iterator function and yield the value until it returns False.
## 3.Use a list comprehension to return the list that is produced by the generator, using the iterator function.
'''
def unfold(fn, seed):
  def fn_generator(val):
    while True: 
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
f = lambda n: False if n > 40 else [-n, n + 10]
print(unfold(f, 10))
'''

##=======================================================================================================================================================================

##4.Write a Python program to create Cartesian product of two or more given lists using itertools.
'''
import itertools
def cartesian_product(l1):
    return list(itertools.product(*l1))
list1=[[1,2],[3,4]]
print(list1)
print(cartesian_product(list1))
list2=[[1,2,3],[3,4,5]]
print(list2)
print(cartesian_product(list2))
'''

##========================================================================================================================================================================

##5.Write a Python program to count the frequency of the elements of a given unordered list by using itertools
'''
from itertools import groupby
l1=[2,1,3,8,5,1,4,2,3,4,0,8,4,3,3,4,2]
l1.sort()
res=[len(list(j)) for i,j in groupby(l1)]
print(res)
'''
