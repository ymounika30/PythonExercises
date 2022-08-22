#WAP to insert string in between the given string
a=input()
b=input()
c=""
for i in a:
    if i!=" ":
        c=c+i
    else:
        c=c+" "+b+" "
print(c)
