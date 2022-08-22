##11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
##INITIAL list :
##58	24	13	15	63	9	8	81	1	78
##
##After spliting :
##58	24	13	15	63
##9	8	81	1	78
a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b+=[c]
n=len(b)
half=n/2
half=int(half)
print(b[:half])
print(b[half:])
