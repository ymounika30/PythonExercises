##1.Find the mean of a list.
def mean_of_list(a):
    sum=0
    for i in a:
        x=int(i)
        sum=sum+x
        y=len(a)
        z=sum/y
        z=int(z)
    return z
a=input().split()
print(mean_of_list(a))
