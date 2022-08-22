a="mississipi"
list_a=[]
for i in a:
    list_a.append(i)
set_a=set(list_a)
for i in set_a:
    x=a.count(i)
    print(i,x)
list_a.sort()
print(list_a)
list_a.sort(reverse=True)
print(list_a)
