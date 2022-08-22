##2)Python Program to Remove the ith Occurrence of the Given Word in a List.
a=input().split()
b=int(input())
for i in range(len(a)):
    if b == i:
        a.pop(i)
        print(a)   
