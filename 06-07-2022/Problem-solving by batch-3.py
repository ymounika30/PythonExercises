##Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes.
##Print all the attributes of student1, student2 instances with their values in the given format.
##
##Input values of the instances:
##student_1:
##student_id = "V12"
##student_name = "Ernesto Mendez"
##student_2:
##student_id = "V12"
##marks_language = 85
##marks_science = 93
##marks_math = 95
##Expected Output:
##student_id -> V12
##student_name -> Ernesto Mendez
##student_id -> V12
##marks_language -> 85
##marks_science -> 93
##marks_math -> 95
class Student:
    def __init__(self):
        self.id=int(input())
        self.name=input()
        self.marks_language=int(input())
        self.marks_science=int(input())
        self.marks_math=int(input())
    def display_1(self):
        print("student_id = ",self.id)
        print("Student_name = ",self.name)
    def display_2(self):
        print("marks_language = ",self.marks_language)
        print("marks_science = ",self.marks_science)
        print("marks_math = ",self.marks_math)
s1=Student()
s1.display_1()
s1.display_2()
