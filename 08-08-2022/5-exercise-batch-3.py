'''1) create a nested list by taking list elements from the user like below
[1,2,[3,4],[5,6,7],8,9]'''

##l=[]
##i=0
##while i<=5:
##    a=eval(input("enter list value: "))
##    l.append(a)
##    i+=1
##print(l)

##==============================================================================================================
'''2) write a program on to retrieve the data from the file and use seek() and tell() method'''
##f=open("data.txt","r")
##print(f.seek(5))
##print(f.tell())
##f.close()
##==============================================================================================================
'''3) write a program on rlock in multithreading'''
##from threading import *
##class Flight:
##    def __init__(self,available_seat):
##        self.available_seat=available_seat
##        self.l=RLock()
##        print(self.l)
##    def reserve(self,need_seat):
##        self.l.acquire()
##        self.l.acquire()
##        print(self.l)
##        print("available seats:",self.available_seat)
##        if(self.available_seat >=need_seat):
##            name=current_thread().name
##            print(f"{need_seat} seat is alloted for {name}")
##            self.available_seat-=need_seat
##        else:
##            print("sorry! all seats are booked")
##        self.l.release()
##        self.l.release()
##f=Flight(2)
##t1=Thread(target=f.reserve,args=(1,),name="Mounika")
##t2=Thread(target=f.reserve,args=(1,),name="Apple")
##t3=Thread(target=f.reserve,args=(1,),name="Cat")
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("Main Thread")
##==============================================================================================================
'''4) wap to create three functions and three threads for each functions and run those threads'''
##from threading import *
##def show1():
##    print("it is function 1")
##def show2():
##    print("it is function 2")
##def show3():
##    print("it is function 3")
##t1=Thread(target=show1)
##t2=Thread(target=show2)
##t3=Thread(target=show3)
##
##t1.start()
##t2.start()
##t3.start()
##==============================================================================================================
'''5) wap to print the next 100th decimal of entered user input 
input = 129, output = 200 , if input = 334, output=400'''

##n=int(input("Enter a Number:"))
##m=100
##while True:
##    if n<m:
##        print(m)
##        break
##    else:
##        m+=100
