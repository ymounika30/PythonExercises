##13.Generate a Python list of all the even numbers between 4 to 30
def list_all_even_nums(a,b):
    list_a=[]
    for i in range(a,b+1):
        if (i%2)==0:
            list_a.append(i)
    return list_a
a=int(input())
b=int(input())
print(list_all_even_nums(a,b))
        
