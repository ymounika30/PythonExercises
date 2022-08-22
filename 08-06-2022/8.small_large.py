##8.Find largest and smallest elements of a list.
a=input()
list_a=[]
for i in a.split():
    list_a+=[int(i)]
print(min(list_a))
print(max(list_a))
