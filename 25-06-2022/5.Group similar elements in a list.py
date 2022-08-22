##5.Group similar elements in a list:
##Input : [1, 3, 5, 1, 3, 2, 5, 4, 2]
##Output : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]
a=input().split()
b=[]
c=[]
for i in sorted(a):
    if a.count(i)<=2:
        b+=[[i,i]]
    else:
        b+=[[i,]]
for i in b:
    if i not in c:
        c+=[i]
print(c)
