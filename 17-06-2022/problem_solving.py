st=list("hello beautiful world")
s=" "
st1=[]
for i in range(len(st)):
    if st[i]==s:
        st1.pop(i-1)
        st[i-1],st[i+1]=st[i+1],st[i-1]
        st1.append(st[i-1])
        st1.append(s)
        st1.append(st[i+1])
        st1.pop(i+1)
    else:
        st1.append(st[i])
print(''.join(st1))


