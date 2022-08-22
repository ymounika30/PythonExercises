##6.Write a Python class to find the three elements that sum to zero from a set of n real numbers.
##Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
##Output : [[-10, 2, 8], [-7, -3, 10]]
class RealNumbers:
    def three_sum(self,a):
        a,b,i=sorted(a),[],0
        while i < len(a)-2:
            j,k=i+1,len(a)-1
            while j<k:
                if a[i]+a[j]+a[k]<0:
                    j+=1
                elif a[i]+a[j]+a[k]>0:
                    k-=1
                else:
                    b.append([a[i],a[j],a[k]])
                    j,k=j+1, k-1
                    while j<k and a[j]==a[j-1]:
                        j+=1
                    while j<k and a[k]==a[k+1]:
                        k-=1
            i+=1
            while i<len(a)-2 and a[i]==a[i-1]:
                i+=1
        return b
print(RealNumbers().three_sum([-25,-10,-7,-3,2,4,8,10]))
        
