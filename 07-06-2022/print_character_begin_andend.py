##Check if a string begins with or ends with a specific character?
a=input()
b=input()
n=len(a)
if (a[0]==b) or (a[n-1]==b):
    print("True")
else:
    print("False")
