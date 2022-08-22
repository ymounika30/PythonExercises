##4.Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
a=int(input())
list_a=[]
list_b=[]
for i in range(a):
    b=int(input())
    list_a+=[b]
list_b=list_a[::-1]
print(list_b)
