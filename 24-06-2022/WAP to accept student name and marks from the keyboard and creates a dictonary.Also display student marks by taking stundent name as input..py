##3)WAP to accept student name and marks from the keyboard and creates a dictonary.Also display student marks by taking stundent name as input.
student={
    "mounika":95,
    "laxmi":70,
    "akhila":50
    }
a=input()
for key,value in student.items():
    if key==a:
        print(value)

