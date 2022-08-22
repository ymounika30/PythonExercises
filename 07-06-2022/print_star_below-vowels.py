#WAP to insert * in front of every vouels in the string.
a=input()
b=""
for i in a:
    if i not in ("a,e,i,o,u"):
        b=b+i
    else:
        b=b+"*"+i
print(b)
    
             
