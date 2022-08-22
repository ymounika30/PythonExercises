a=int(input("Enter a input:"))
b=int(input("Enter b input:"))
print("* "*b)
for i in range(a-2):
    space="  "*(b-2)
    star="* "+space+"* "
    print(star)
print("* " *b)
