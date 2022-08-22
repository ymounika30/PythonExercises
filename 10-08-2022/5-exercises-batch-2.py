'''1.Python Program to Reverse a Stack using Recursion'''

##from collections import deque
##def insertAtBottom(s, item):
##    if not s:
##        s.append(item)
##        return
##    top = s.pop()
##    insertAtBottom(s, item)
##    s.append(top)
##def reverseStack(s):
##    if not s:
##        return
##    item = s.pop()
##    reverseStack(s)
##    insertAtBottom(s, item)
##s = deque(range(1, 6))
##reverseStack(s)
##print(s)
##====================================================================================================================================
'''2.Python Program to Append the Content of One File to the End of Another File'''
##a=input()
##b=input()
##f1=open(a,"r")
##f2=f1.read()
##f1.close()
##f3=open(b,"a")
##f3.write(f2)
##f3.close()
##====================================================================================================================================
'''3.Python Program to Create a Class and Get All Possible Distinct Subsets from a Set'''
##class Unique_Subsets:
##    def sub_sets(self,a):
##        return self.recurr([],sorted(a))
##    def recurr(self,b,a):
##        if a:
##            return self.recurr(b,a[1:])+self.recurr(b+[a[0]],a[1:])
##        return [b]
##print(Unique_Subsets().sub_sets([1,2,3]))
##====================================================================================================================================
'''4.How can you randomize the items of a list in place in Python?'''
##import random
##a=[11,21,2,100]
##random.shuffle(a)
##print(a)
##====================================================================================================================================
'''5.write a python program on showing 
KeyboardInterrupt,
ArithmeticError,
StopIteration
AssertionError
ImportError
'''
##try:
##    a=input()
##    print("Keyboard Interrupt")
##except KeyboardInterrupt:
##    print("KeyboardInterrupt exception")
##else:
##    print("Exception thrown")

##try:
##    srithmetic=5/0
##    print(arithmetic)
##except ArithmeticError:
##    print("Arithmetic Error exception")

##a=[1,2,3]
##b=iter(a)
##print(next(b))
##print(next(b))
##print(next(b))
##print(next(b))


##a=1
##b=0
##assert b!=0, "Invalid exception"
##print(a/b)

##from itertools import abc
