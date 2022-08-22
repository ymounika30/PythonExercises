##9.Write a program to print sum, average of all numbers, smallest and largest element of a list.
a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b+=[c]
print(sum(b))
print(int(sum(b)/len(b)))
print(min(b))
print(max(b))
