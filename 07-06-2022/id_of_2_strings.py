#How would you confirm that 2 strings have the same identity?
a=10
b=20
a=b
if id(a)==id(b):
    print("True")
else:
    print("False")
    
