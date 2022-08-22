##2.write a program to count number of chareters and print accending and desending order
##input:RameshRam
##output:a-2,e-1,h-1,m-2,R-2,s-1- assending
##decending :s-1,R-2m-2,,h-1,e-1a-2,
a=input()
b=[]

for i in a:
    if i not in b:
        b+=[i]
for i in b:
    print(i,"-",a.count(i), end=" ")
print()
for i in sorted(b):
    print(i,"-",a.count(i), end=" ")
print()
for i in sorted(b)[::-1]:
    print(i,"-",a.count(i),end=" ")
