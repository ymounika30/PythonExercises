##3..find the smallest word in the given sentences and length?
##ex:-input:-this is mounika
##output:-is -2
a=input().split()
b=[]
c=[]
for i in a:
    n=len(i)
    b+=[n]
print(min(b))
