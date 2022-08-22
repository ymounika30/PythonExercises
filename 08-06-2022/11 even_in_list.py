##12.
##Ask user to give integer inputs to make a list. Store only even values given and print the list.
a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b+=[c]
print(b)
list_a=[]
for i in b:
    x=int(i)
    if (x%2)==0:
        list_a+=[x]
print(list_a)
