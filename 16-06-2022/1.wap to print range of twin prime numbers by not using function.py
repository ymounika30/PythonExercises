# wap to print range of twin prime numbers by not using function'''
n=int(input())
for i in range(n):
 if i >1:
    for j in range(2,i):
     if i%j==0:
       break
     else:
         x=i+2
         for k in range(2,x):
             if x%k==0:
                 break
             else:
                 print(i,x)
