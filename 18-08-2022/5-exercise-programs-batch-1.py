'''1).Write a Python program to remove and print every third number from a list of numbers until the list becomes empty'''
##a=[10,20,30,40,50,60,70,80,90]
##b=2
##c=0
##n=len(a)
##while n>0:
##    c=(c+b)%n
##    print(a.pop(c))
##    n-=1
    
##=========================================================================================================================================================================================
'''2).. Write a Python program to count the number of students of individual class.
Sample Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})'''
##from collections import Counter
##classes = (
##    ('V', 1),
##    ('VI', 1),
##    ('V', 2),
##    ('VI', 2),
##    ('VI', 3),
##    ('VII', 1),
##)
##students = Counter(class_name for class_name, no_students in classes)
##print(students)
##==========================================================================================================================================================================================
'''3).Write a Python program to concatenate all elements in a list into a string and return it'''
##a=[1,2,3,4]
##b=""
##for i in a:
##    b=b+str(i)
##print(b)
##==========================================================================================================================================================================================
'''4).Write a Python program to convert a float to ratio. 
Expected Output :21/5'''
##from fractions import Fraction
##value = 4.2
##z = Fraction(value).limit_denominator()
##print(z)
##==========================================================================================================================================================================================
'''5).Write a Python function that prints out the first n rows of Pascal’s triangle'''
##def pascal_triangle(n):
##   trow = [1]
##   y = [0]
##   for x in range(max(n,0)):
##      print(trow)
##      trow=[l+r for l,r in zip(trow+y, y+trow)]
##   return n>=1
##pascal_triangle(6)
