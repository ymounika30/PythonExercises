#Write a program to find all palindrome in a given range.
a=int(input())
b=int(input())
for i in range(a,b+1):
    x=str(i)
    if x==x[::-1]:
        print(x)
