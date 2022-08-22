#3) wap to print even and odd numbers separatly from a list by using filter function.'''

lst=[1,2,3,4,5,6,7,8,22,54,6,8]
res=filter(lambda x:x%2==0,lst)
print(list(res))
res=filter(lambda x:x%2!=0,lst)
print(list(res))
