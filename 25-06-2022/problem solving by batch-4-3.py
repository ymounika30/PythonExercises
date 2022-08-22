##given alist of integers write a program to print the count of all possible unique combinations of numbers whose sum is equal to k
##explanation:for example if given list of integers and k are 
##2 4 6 1 3
##6
##all possible combinations of the given list are
##(6,)(2,)(4,)(1,)(3,)
##(2,4)(1,2)(3,4)(4,6)(1,4)(2,3)(2,6)(3,6)(1,6)(1,3)
##(3,4,6)(2,3,6)(1,2,6)(1,2,3)(1,4,6)(1,3,4)(2,3,4)(1,3,6)
##(2,3,4,6)(1,2,3,4)(1,2,4,6)(1,2,3,6)(1,3,4,6)
##out of all the above combinations  the unique combinations with the sum equal to 6 are
##6
##2 4
##2 1 3
##so the output should be the count of unique combinations which is 3
##for example if the given list of integers and k are
##-1 4 5 6 7 8 2 4 5 2 3 8
##7
##The unique combinations with the sum equal to 7 are
##7
##-1 8
##3 4
##2 5
##-1 3 5
##-1 4 4
##-1 2 6
##2 2 3
##-1 2 2 4
##so the output should be the count of unique combinations which is 9
##input:  2 4 6 1 3
##         6
##output:  3
##Note: Dont use permutations and combiations method
def combi(a,r):
    if r==0:
        return [[]]
    l=[]
    x=len(a)
    for i in range(x):
        first=a[i]
        rem=a[i+1:]
        total=combi(rem,r-1)
        for j in total:
            p=([first]+j)
            p.sort()
            if p not in l:
                l.append(p)
    return l
s=input()
k=int(input())
a=[]
for i in s.split():
    t=int(i)
    a+=[t]
b=len(a)
c=[]
for i in range(1,b+1):
    d=combi(a,i)
    for sub in d:
        if sum(sub)==k:
            c+=[sub]
print(len(c))
    
    
