#WAP to print half reverse of the string
a=input()
n=0
for i in a:
    n=n+1
m=n/2
m=int(m)
print(a[m:][::-1]+a[:m])
