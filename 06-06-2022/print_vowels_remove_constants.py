a=input()
vowels="a,e,i,o,u"
b=""
c=""
for i in a:
    if i not in (vowels):
        c=c+i
    elif i in (vowels):
        b=b+i
print(b)
print(c)
