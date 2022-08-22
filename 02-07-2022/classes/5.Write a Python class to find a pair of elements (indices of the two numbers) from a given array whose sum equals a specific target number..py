##5.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
##Input: numbers= [10,20,10,40,50,60,70], target=50
##Output: 3, 4
class Pairofelements:
    def sum_two(self,a,b):
        c={}
        for i,j in enumerate(a):
            if b-j in c:
                return (c[b-j],i)
            c[j]=i
print(Pairofelements().sum_two((10,20,10,40,50,60,70),50))
