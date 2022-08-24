##Write a  Python Program using Multithreading ,
##Consider a couple who is having a Joint account and both are having their ATM cards.
##They come to different ATMs and try to withdraw some amount at the same time.
##Let’s say the total balance in the account is 500 and Wife tries to withdraw 450
##and the husband tries to withdraw 100. When they swipe the card for withdrawing money,
##the balance shown will be 500. Two threads will be created for the transaction,
##out of which only one thread should be successful and the other should fail.
##If both the threads get successful then its a loss to the bank.
##So, the threads should be in synchronization so that one fails and the other wins.
from threading import *
class ATM:
    def __init__(self,a):
        self.a=a
        self.l=Lock()
        print("current balance in joint ac: ",self.a)
    def wife(self,w):
        if w<=self.a:
            self.l.acquire(blocking=True)
            self.a-=w
            print(f"{w} amount withdraw success")
            print("current balance in joint ac: ",self.a)
        else:
            print("sorry insuffient balance: ",self.a)
        self.l.release()
    def hus(self,w):
        self.l.acquire(blocking=True)
        if w<=self.a:
            self.a-=w
            print(" amount withdraw success",w)
            print("current balance in joint ac: ",self.a)
        else:
            print("sorry insuffient balance: ",self.a)
        self.l.release()
s=ATM(10000)
t1=Thread(target=s.wife,args=(500,))
t2=Thread(target=s.hus,args=(9000,))
t3=Thread(target=s.wife,args=(1000,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
