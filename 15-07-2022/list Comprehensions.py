"""numbers only"""
##a=[1,2,1,3]
##l1=[i for i in a]
##print(l1)

"""Factorial of Number using list comprehension."""

##import math
##
##n=[math.factorial(i) for i in range(1,10)]
##print(n)

##import math
##
##n=[math.factorial(i) for i in range(1,10)]
##print(n)

"""fibonacci of number using list Comprehension"""
##n=10
##a=[0,1]
##[a.append(a[-2]+a[-1])for n in range(10)]
##print(a)

##n=10
##a=[0,1]
##[a.append(a[-2]+a[-1] )for n in range(10)]
##print(a)

"""Permutations of a number"""

##from itertools import permutations
##comb="abc"
##
##d=list(permutations(comb))
##print(d)

##l1=["a","b","c","d"]
##l2=[i for i in l1]
##print(l2)

##l1=["a","b","c","d"]
##
##l2=[i for i in l1 if i!="a"]
##print(l2)

##l1=["a","b","c","d"]
##l2=[i.upper() for i in l1]
##print(l2)

##l=[0,1,2,3,4,5,6,7,8,9,10]
##
##l1=[i+1 for i in l]
##print(l1)
##
##l=[i+1 for i in range(2,20)]
##print(l)
##l=[i if i%2==0 else "Invalid"for i in range(10)]
##print(l)

##l1=['a','b']
##l2=[1,2]
##l3=[i+str(j) for  i in l1 for j in l2]
##print(l3)

##l1=["billy@gmail.com", "george@hotmail.com","www.billy.com","python.com", "mike@predictivehacks.com"]
##domains=['gmail.com',"hotmail.com"]
##
##l2=[i for i in l1 for j in domains if j in str(i)]
##print(l2)


##l1=["a","b","c","d","e","f"]
##l2={i:j for i,j in enumerate(l1)}
##
##print(l2)

##l1=["a","b","c","d","e","f"]
##l2={i:i*2 for i in l1}
##print(l2)

""" Dict Comprehension"""

##d1={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
##
##d2={key+2:value for key,value in d1.items()}
##print(d2)
"""Set Comphrehension"""
##set2={i for i in range(20) if i%2==0}
##print(set2)
##
##set={i for i in range(20) if i%2==0 if i%3==0}
##print(set)
##s={i if i%2==0 else i*1000 for i in range(10)}
##
##print(s)

##s={(i,j) for j in range(10,13) for i in range(6,8)}
##print(s)
#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

##def func(n):
##    return lambda x:x*n
##
##res=func(2)
##print("Double of the  Number 14 is:",res(14))

##l=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
##res=dict(map(lambda x:(x,list(l).count(x)),l))
##print(res)

##Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function
##class_students = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
##return_max=max(class_students,key=lambda item:item[1])[1]
##return_min=min(class_students,key=lambda item:item[1])[1]
##
##print(return_max)
##print(return_min)

##Write a Python program to remove specific words from a given list using lambda.

##colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
##
##remove_colors = ['orange','black']
##
##res=list(filter(lambda colors: colors not in remove_colors,colors))
##print(res)

##def fact(n):
##    if n==1:
##        return 1
##    else:
##        return(n*fact(n-1))
##
##num=int(input("Enter a Number:"))
##result=fact(num)
##print("The Factorial of {} Is :{}".format(num,result))

##def fib(n):
##    if n<=1:
##        return n
##    else:
##        return fib(n-1)+fib(n-2)
##
##n=int(input("Enter a Number:"))
##print("The Fibonacci of {} is {}".format(n,fib(n)))
##

l=[10,20,22,25,28,30,31]

##l2=list(map(lambda x:x if x%2==0 else "Odd",l))
##print(l2)

l1=list(filter(lambda x: x if x%2==0 else))
print(l1)
