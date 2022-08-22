##5.write a program about ojas organization parent class is ojas and child class is OILC write differnt batches as methods define batchs name with inheritance.
class Ojas:					
	def __init__(self, name,empid):
		self.name = name
		self.empid=empid
		
	def show(self):
		print("Ojas employee name: ", self.name)
		print("Ojas employee id: ", self.empid)
		
		
class OILC(Ojas):				
	def __init__(self, course, empid, name):
		super().__init__(empid, name)
		self.course = course
		
	def disp(self):
		print("OILC Course", self.course)

s = OILC('Python',"Mounika",22114)
s.disp()
s.show()

    
