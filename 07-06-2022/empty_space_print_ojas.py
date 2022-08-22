a=input()
b=" "
c=""
for i in a:
    if i not in b:
        c=c+i
    else:
        c=c+" ojas"+i
print(c)
