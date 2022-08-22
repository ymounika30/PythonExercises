#WAP to remove all the vouels from the given string
a=input()
b=""
for i in a:
    if i not in ("a,e,i,o,u"):
        b=b+i
print(b)
