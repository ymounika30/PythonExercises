##14.Return the largest item from the given list
def largest_item(a):
    list_a=[]
    for i in a.split():
        list_a+=[i]
        x=max(list_a)
    return x
a=input()
print(largest_item(a))
