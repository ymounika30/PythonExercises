##1.write a program to count number of words and print accending and
##desending order
##input:this is a mounika and mounika team :
##this-1
##is-1
##a-1
##mounika-2
##and-1
##team-1
a=input().split()
b=[]
for i in a:
    if i not in b:
        b+=[i]
for i in sorted(b):
    print(i,a.count(i))
for i in sorted(b)[::-1]:
    print(i,a.count(i))

