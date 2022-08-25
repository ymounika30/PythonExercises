from threading import Thread

class Mythread(Thread):
	def __init__(self, a):
		Thread.__init__(self)		# Calling Thread Class(Parent) Constructor
		print("Thread Constructor", a)
	def run(self):
		pass

t = Mythread(10)
t.start()
print("Main Thread")
