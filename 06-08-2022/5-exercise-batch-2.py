'''1.write a program to count elements in a file?'''
##with open ("data.txt","r") as f:
##    line=len(f.readlines())
##    print(line)
##==============================================================================================================================
'''2.write a python program on atleast three magic methods?'''
##class magic:
##    def __init__(self,a):
##        self.a=a
##    def __str__(self):
##        return f"The Name is {self.a}i am str method"
##
##    def __repr__(self):
##        return f"The Name is {self.a}"
##    def __add__(self,c):
##        return self.a+c.a
##e=magic("Mounika")
##e1=magic("Laxmi")
##print(e)
##print(repr(e))
##print(e+e1)
##==============================================================================================================================
'''3.Write python program on multithreading?'''
##import threading
##def square(a):
##    for i in a:
##        print(i**2)
##def cube(a):
##    for i in a:
##        print(i**3)
##a=[1,2,3,4,5]
##t=threading.Thread(target=square,args=(a,))
##t1=threading.Thread(target=cube,args=(a,))
##t.start()
##t1.start()

##==============================================================================================================================
'''4.Write a dictionary to a file in Python'''
##diict = {1:1, 2:2, 3:3}
##with open('data.txt', 'w+') as f:
##    f.write(str(diict))
##==============================================================================================================================
'''5.write the program to Get Yesterday’s date using Python?'''
##from datetime import*
##today = date.today()
##print("Today is: ", today)
##yesterday = today - timedelta(days = 1)
##print("Yesterday was: ", yesterday)
