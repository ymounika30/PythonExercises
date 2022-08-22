##6.Write a program to find the product of all elements of a list.
a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b+=[c]
print(b)
p=1
for i in b:
    p=p*i
print(p)
