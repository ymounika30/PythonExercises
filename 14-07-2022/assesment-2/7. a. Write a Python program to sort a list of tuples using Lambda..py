##7. 	a. Write a Python program to sort a list of tuples using Lambda.
##Original list of tuples:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##Sorting the List of Tuples:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
marks=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(marks)
marks.sort(key=lambda x:x[1])
print(marks)
'''
##Output:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


##b.Write a Python program to create Fibonacci series upto n using Lambda
'''
from functools import reduce
fib=lambda b:reduce(lambda a,x:a+[a[-1]+a[-2]],range(b-2),[0,1])
print(fib(10))
'''
##Output:
##[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

##c.Write a Python program to add two given lists using map and lambda.
'''
l1=[1,2,3,4]
l2=[4,5,6,7]
result=map(lambda a,b:a+b,l1,l2)
print(list(result))
'''
##Output:
##[5, 7, 9, 11]

##d. Write a Python program to find palindromes in a given list of strings using Lambda.  
##Orginal list of strings:
##['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##List of palindromes:
##['php', 'aaa'] 
l1=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print(l1)
x=list(filter(lambda x: (x=="".join(reversed(x))),l1))
print(x)

##Output:
##['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##['php', 'aaa']


##e. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
##(Hint: lambda will be passed to sort method's key parameter as argument)





##
##f. Write a lambda function which takes z as a parameter and returns z*11

f=lambda z:z*11
print(f(5))

##Output:
##55
