##write a python program using basic mathematic operations like 
##addition, subtraction, multiplication, division,floor division 
##by applying multithreading concept
import threading
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def floor_div(a,b):
    print(a//b)
b=[add,sub,mult,div,floor_div]
for i in b:
    t=threading.Thread(target=i,args=(1,20))
    t.start()
    t.join()

