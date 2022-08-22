##2.wap take a string sparate with space and done add,sub,mul,div?
##eg:- input:-18 7
##     output:-(25,12,126,2)
a=input().split()
b=[]
for i in a:
    b+=[int(i)]
x=b[0]+b[1]
y=b[0]-b[1]
z=b[0]*b[1]
p=b[0]//b[1]
print((x,y,z,p))
