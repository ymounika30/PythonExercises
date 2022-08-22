##1.How do you print duplicate characters from a string?
a=input()
b=[]
s=""
for i in a.split():
    s=s+i
x=len(s)
p=[]
l=""
for i in range(x):
    c=0
    for j in range(i+1,x):
        if (s[i]==s[j]) and (s[i] not in p):
            c+=1
    if c>0:
        p+=s[i]
        print(s[i])
