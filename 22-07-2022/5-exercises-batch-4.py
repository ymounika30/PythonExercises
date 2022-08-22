##1.Write a python program in fibonacci series using generator
'''
def fib(a):
    x=0
    y=1
    for i in range(a):
        yield x
        x,y=y,x+y
for i in fib(10):
    print(i)
 '''       
##===========================================================================================================
##2.Write a python program to generate the running product of the elemnts of a given iterable
'''
from itertools import accumulate
import operator as op
def running_product(a):
    return accumulate(a,op.mul)
#List
result = running_product([1,2,3,4,5,6,7])
print("Running product of a list:")
for i in result:
    print(i)

#Tuple
result = running_product((1,2,3,4,5,6,7))
print("Running product of a Tuple:")
for i in result:
    print(i)
'''
##===============================================================================================================
##3.factorial using iterators
'''
import itertools as it
import operator as op
def fact(a):
    res=list(it.accumulate(it.chain([1], range(1,1+a)),op.mul))
    return res
print(fact(5))
'''
##============================================================================================================================
##4.Write a simple registeration form which contains input buttons heading and radio buttons
'''
from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_2 = Entry(root)
entry_2.place(x=240,y=280)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
root.mainloop()
print("registration form  seccussfully created...")
'''
##================================================================================================================================================
##5.prime progam using sys module
'''
from sys import *

for j in range(2,int(argv[1])):
    if int(argv[1])%j==0:
        print("This  Number is not Prime.")
        break

else:
    print("This Number is Prime.")
'''
