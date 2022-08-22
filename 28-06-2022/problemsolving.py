##Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda.
##Input number of students, names and grades of each student.
##
##Note: If there are multiple students with the same grade then print each name alphabetically.
##
##sample out:
##Input number of students:  5
##Name:  S ROY
##Grade:  1
##Name:  B BOSE
##Grade:  3
##Name:  N KAR
##Grade:  2
##Name:  C DUTTA
##Grade:  1
##Name:  G GHOSH
##Grade:  1
##
##Names and Grades of all students:
##[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
##
##Second lowest grade:  2.0
##
##Names:
##N KAR


students=[]
sec_name=[]
second_low=0
a=int(input("number of students: "))
for i in range(a):
    b=input("student name: ")
    c=float(input("student grade: "))
    students+=[(b,c)]
order=sorted(students,key=lambda x: int(x[1]))
for i in range(a):
    if order[i][1]!=order[0][1]:
        second_low=order[i][1]
        break
print("Second lowest grade: ", second_low)
sec_student_name=[x[0] for x in order if x[1]==second_low]
sec_student_name.sort()
for i in sec_student_name:
    print("Second lowest name: ", i)
    
