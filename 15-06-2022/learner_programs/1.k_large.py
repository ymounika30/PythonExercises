##1 write a program to print the kth largest number in the list
a=input().split(",")
b=int(input())
n=len(a)
for i in range(n):
    a[i]=int(a[i])
a=sorted(a)
k_large=a[-b]
print(k_large)
