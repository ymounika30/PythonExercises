'''
import threading
t=threading.current_thread().getName()
print(t)
'''
##=======================================================================================
'''
import threading
def disp():
    print("Thread Running")
t=threading.Thread(target=disp)
t.start()
'''
##=======================================================================================
'''
import threading
def disp(a,b):
    print("Thread Running", a,b)
t=threading.Thread(target=disp, args=(10,20))
t.start()
'''
##=======================================================================================
'''
import threading
def disp(a,b):
    print("Thread Running", a, b)
for i in range(5):
    t=threading.Thread(target=disp, args=(10, 20))
    t.start()
'''
##=======================================================================================
'''
import threading
def disp():
    for i in range(5):
        print("Child Thread")
t=threading.Thread(target=disp)
t.start()
for i in range(5):
    print("Main Thread")
'''
##=======================================================================================
'''
from threading import Thread, current_thread
def disp():
	print("Child Thread", current_thread())
	print("Default Child Thread Name:", current_thread().getName())
	current_thread().setName('Doc Thread')
	print("New Child Thread Name:", current_thread().getName())
	current_thread().name = 'Flying Thread'
	print(current_thread().name)
t = Thread(target=disp)
t.start()
print("Main Thread", current_thread())
print("Default Main Thread Name:", current_thread().getName())
current_thread().setName('ojas Thread')
print("New Main Thread Name:", current_thread().getName())
current_thread().name = 'new Thread'
print(current_thread().name)
'''
##=======================================================================================
'''
from threading import Thread
def disp():
	pass
t = Thread(target=disp)
print("Default Child Thread Name:",t.getName())
t.setName('Doc Thread')
print("New Child Thread Name:",t.getName())
t.name = 'Flying Thread'
print(t.name)
'''
##=======================================================================================
'''
from threading import Thread
def disp():
	pass
t = Thread(target=disp, name='Raj Thread')
print(t.name)
'''
##=======================================================================================
'''
from threading import Thread
class Mythread(Thread):
	pass
t = Mythread()
print(t.name)
'''
