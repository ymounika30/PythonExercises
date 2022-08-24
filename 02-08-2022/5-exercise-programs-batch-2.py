'''1. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.'''
##def consecutive(a):
##    while "01" in a:
##        a=a.replace("01","")
##    return len(a)==0
##a="01010101"
##print(consecutive(a))

##===============================================================================================================================================================================
'''2. Write a Python program to add more number of elements to a deque object from an iterable object.'''
##import collections
##nums=(2,3,5,7)
##deque=collections.deque(nums)
##print(deque)
##more_nums=(11,13,17)
##deque.extend(more_nums)
##print(deque)
##===============================================================================================================================================================================
'''3.Reverse a list without using inbuit method and [::-1]'''
##a=[1,2,3,4,5]
##n=len(a)-1
##for i in range(len(a)//2):
##    a[i],a[n]=a[n],a[i]
##    n=n-1
##print(a)

##==============================================================================================================================================================================
'''4.cummulative sum of a list'''
##a=[1,2,3,4,5]
##b=0
##for i in a:
##    b=b+i
##print(b)
##===============================================================================================================================================================================
'''5.write one example for pickling and unpickling?'''
##import pickle
##a={"name":"Mounika","id":22114}
##with open("student.txt","wb") as f:
##    pickle.dump(a,f)
##with open("student.txt","rb") as f:
##    x=pickle.load(f)
##    print(x)
