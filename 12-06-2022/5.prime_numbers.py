##5.Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
def prime_numbers(a):
    for i in range(1,a+1):
        f=0
        for j in range(2,i+1):
            if (i%j)==0:
                f=f+1
        if f==1:
            print(i)
a=int(input())
prime_numbers(a)
