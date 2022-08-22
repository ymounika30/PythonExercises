##Given a sentence as input print all the unique combinations of two words in lexicographical order
##explanation:
##if given sentence is raju plays cricket the possible combintion of two are (cricket,plays),(cricket,raju),(plays,raju).
##input:
##raju plays cricket
##output:
##cricket plays
##cricket raju
##plays raju
a=input().split()
x=len(a)
b=[]
for i in range(x):
    for j in range(i+1,x):
        y=sorted([a[i],a[j]])
        b+=[y]
b.sort()
for i in  b:
    print(i[0]+" "+i[1])
