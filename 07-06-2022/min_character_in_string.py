#Return the minimum character in a string
a=input()
list_a=[]
for i in a:
    x=ord(i)
    list_a+=[x]
print(i,(min(list_a)))

