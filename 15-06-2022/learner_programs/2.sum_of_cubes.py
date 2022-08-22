##2 write a function with name sum of cubes a to b that takes two integers and sum of the cubes from a to b
def sum_of_cubes(a,b):
    s=0
    for i in range(a,b+1):
        x=i**3
        s=s+x
    return s
a=int(input())
b=int(input())
print(sum_of_cubes(a,b))
