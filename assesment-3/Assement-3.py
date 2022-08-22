##1. 4.Write a Python class to get all possible unique subsets from a set of distinct integers.
##Input : [4, 5, 6]
##Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
'''
class Unique_Subsets:
    def sub_sets(self,a):
        return self.recurr([],sorted(a))
    def recurr(self,b,a):
        if a:
            return self.recurr(b,a[1:])+self.recurr(b+[a[0]],a[1:])
        return [b]
print(Unique_Subsets().sub_sets([4,5,6]))
'''
##Output:
##[[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
        
##================================================================================================================================================================================================
##2. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
##Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
##Output : [[-10, 2, 8], [-7, -3, 10]]
'''
class Real_Numbers:
    def three_sum(self,a):
        a,result,i=sorted(a),[],0
        while i < len(a)-2:
            j,k=i+1,len(a)-1
            while j<k:
                if a[i]+a[j]+a[k]<0:
                    j+=1
                elif a[i]+a[j]+a[k]>0:
                    k-=1
                else:
                    result.append([a[i],a[j],a[k]])
                    j,k=j+1,k-1
                    while j<k and a[j]==a[j-1]:
                        j+=1
                    while j<k and a[k]==a[k+1]:
                        k-=1
            i+=1
            while i<len(a)-2 and a[i]==a[i-1]:
                i+=1
        return result
print(Real_Numbers().three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))
'''
##Output:
##[[-10, 2, 8], [-7, -3, 10]]
##================================================================================================================================================================================================

##3. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case
'''
class Print_Get():
    def __init__(self):
        self.a=""
    def get_string(self):
        self.a=input()
    def print_string(self):
        print(self.a.upper())
s=Print_Get()
s.get_string()
s.print_string()
'''
##Output:
##Mounika
##MOUNIKA
##================================================================================================================================================================================================
##4. Write a Python program to count the frequency of words in a file
'''
import collections
def count(fname):
    with open(fname) as f:
        return collections.Counter(f.read().split())
print(count("task.txt"))
'''
##Output:
##Counter({'your': 4, 'to': 3, 'names': 2, 'code': 2, 'it': 2, 'make': 2, 'Choosing': 1, 'for': 1, 'variables,': 1, 'functions,': 1, 'classes,': 1, 'and': 1, 'so': 1,
##         'forth': 1, 'can': 1, 'be': 1, 'challenging.': 1, 'You': 1, 'should': 1, 'put': 1, 'a': 1, 'fair': 1, 'amount': 1, 'of': 1, 'thought': 1, 'into': 1, 'naming': 1,
##         'choices': 1, 'when': 1, 'writing': 1, 'as': 1, 'will': 1, 'more': 1, 'readable.': 1, 'The': 1, 'best': 1, 'way': 1, 'name': 1, 'objects': 1, 'in': 1, 'Python': 1,
##         'is': 1, 'use': 1, 'descriptive': 1, 'clear': 1, 'what': 1, 'the': 1, 'object': 1, 'represents.': 1})
##================================================================================================================================================================================================
##5. .Write a Python program to extract characters from various text files and puts them into a list.
'''
import glob
b=[]
c=glob.glob("*.txt")
for i in c:
    with open(i,"r") as f:
        b.append(f.read())
print(b)
'''
##Output:
##['Choosing names for your variables, functions, classes, and so forth can be challenging.\nYou should put a fair amount of thought into your naming choices when writing code as it \nwillmake your code more readable. The best way to name your objects in Python is to use \ndescriptive names to make it clear what the object represents.']
##================================================================================================================================================================================================
##6. Write a Python program to generate the running product of the elements of an given iterable.
'''
import itertools
import operator
def running_product(itert):
    return itertools.accumulate(itert,operator.mul)
res=running_product([1,2,3,4,5,6,7,8,9])
for i in res:
    print(i)
'''
##Output:
##1
##2
##6
##24
##120
##720
##5040
##40320
##362880
##================================================================================================================================================================================================
##7. A class Student is given to you. Add details in the Student class.
##Student:
##Instance Variables: studentId : PUBLIC , studentName : PUBLIC ,
##Marks: PRIVATE, grade: PRIVATE
##PUBLIC Methods: displayDetails(): ,
##PRIVATE METHOD : calculateGrade():
##Default constructor
##A constructor that that takes the following parameter: studentId, studentName, marks.
##Note that grade is not set either through constructor or setter as it is a calculated value.
##Methods
##displayDetails(): This method should display the details of the student in the following format:
##Student [name=John Smith, studentId=123, marks=95, grade=A]
##calculateGrade(): This is a private method that calculates the grade based on the marks that is set. If marks is above 90, grade is set to A. If marks is between 80 and 90,
##grade is set to B, if marks is between 70-80 grade is set to C, if marks is between 60-70, grade is set to D, if marks is less than 60, grade is set to E.Use this method when you
##need to set or reset grade
'''
class Student:
    def __init__(self,studentName,studentId,__marks,__grade):
        self.studentName=studentName
        self.studentId=studentId
        self.__marks=__marks
        self.__grade=__grade
    def displaydetails(self):
        print(self.studentId)
        print(self.studentName)
        print(self.__marks)
        print(self.__grade)
    def __calculateGrade(self,_grade):
        self.__grade=grade
        a=90
        b=80
        if self.__marks>a:
            print("A")
        if self.__marks>=b:
            print("B")
s=Student("MOunika",22114,90,"A+")
s.displaydetails()
'''
##Output:
##22114
##MOunika
##90
##A+

##================================================================================================================================================================================================
##8. In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year), separated by comma / space or both and return the date in the format of YYYY-MM-DD.
##
##Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012
##
##Output : 2012-05-21
##
##Note the following:
##
##The input can have comma, space or both. No other separator is allowed
##
##The month can be given in full form (January, February etc) or in short 3-Letter form (Jan, feb,mar, apr, may, jun, jul, aug, sep, oct, nov, dec) . This program should accept both types.
##
##Output month should always be a number.
##
##Validate for invalid values.
##
##Return null for error in input.
'''
from datetime import date
class Dateformatter:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def format(self):
       
       print((self.year,self.month,self.date))
a=Dateformatter(21,"july",2022)
a.format()
'''
#Output:
##(2022, 'july', 21)
##================================================================================================================================================================================================
##9. Write a python program on filtering consonants
##
##Note the following points:
##
##1. The method should scan the given input, remove all the consonants and return the resulting string.
##
##2. The output should contain only vowels and all other characters, including special characters should be filtered out.
##
##3. If input is null, return null.
##
##4. Example input: “Telephone”, Output: “eeoe”
'''
a=input("enter a string: ")
b=""
for i in a:
    if i in ("a","e","i","o","u"):
        b=b+i
print(b)
'''
##Output:
##enter a string: Telephone
##eeoe
##================================================================================================================================================================================================
##10. Write a python program to find factorial , Fibonacci series, sum of digits, product of digits, reverse of a number, amstrong number.
'''
def outer(a):
    def inner():
        x=int(input("enter a number: "))
        fact=1
        for i in range(1,x+1):
            fact=fact*i
        print(fact)
    return inner
@outer
def new():
    pass
new()
'''
##Output:
##enter a number: 7
##5040

'''
def outer(a):
    def inner():
        x=int(input("enter a number: "))
        a=0
        b=1
        for i in range(x):
            c=a+b
            a=b
            b=c
            print(c)
    return inner
@outer
def new():
    pass
new()
'''
##Output:
##enter a number: 7
##1
##2
##3
##5
##8
##13
##21

'''
def outer(a):
    def inner():
        x=int(input("enter a number: "))
        b=0
        for i in range(1,x+1):
            b=b+i
            print(b)
    return inner
@outer
def new():
    pass
new()
'''
##Output:
##1
##3
##6
##10
##15
'''
def outer(a):
    def inner():
        x=int(input("enter a number: "))
        b=1
        for i in range(1,x+1):
            b=b*i
            print(b)
    return inner
@outer
def new():
    pass
new()
'''
##Output:
##enter a number: 5
##1
##2
##6
##24
##120

'''
def outer(a):
    def inner():
        x=int(input("enter a number: "))
        n=x
        b=0
        while x>0:
            dig=x%10
            b=b*10+dig
            x=x//10
        print(b)
    return inner
@outer
def new():
    pass
new()
'''
##Output:
##enter a number: 121
##Number is Reversed
##enter a number: 133
##Number is not reversed

'''
def outer(a):
    def inner():
        p=int(input("enter a number: "))
        n=len(str(p))
        b=0
        x=p
        while(x>0):
            c=x%10
            b=b+c**n
            x=x//10
        if p==b:
            print("Armstrong")
        else:
            print("Not a Armstrong")
    return inner
@outer
def new():
    pass
new()
'''
##Output:
##enter a number: 153
##Armstrong
##enter a number: 1642
##Not a Armstrong
