##1. Define a function that accepts roll number and returns whether the student is present or absent.
def roll_num(a):
    x=[30,45,2,7,11,19]
    if a in x:
        print(f"Roll number {a} is present")
    else:
        print(f"Roll number {a} is absent")
a=int(input())
roll_num(a)
