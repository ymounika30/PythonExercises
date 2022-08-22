##3.Collatz Sequence
a=int(input())
if a%2==0:
    a=a//2
else:
    a=3*a+1
print(a)
