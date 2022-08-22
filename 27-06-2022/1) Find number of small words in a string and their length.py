##1) Find number of small words in a string and their length?
##eg:-This is an offical page
##output:- is-2 
##         an-2 
a=input().split()
b=[]
for i in a:
    n=len(i)
    b+=[n]
x=min(b)
for j in a:
    if len(j)==x:
        print(j,len(j))
