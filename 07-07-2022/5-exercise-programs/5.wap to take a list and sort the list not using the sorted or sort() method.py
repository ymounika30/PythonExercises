##5.wap to take a list and sort the list not using the sorted or sort() method
##input:  [2,5,12,6,1,4]
##output:   [1,2,4,5,6,12]
##and not using max() or min() method

##list_a=[]
##while a:
##    minimum=a[0]
##    for x in a:
##        if x<minimum:
##            minimum=x
##    list_a.append(minimum)
##    a.remove(minimum)
##l=[64,25,1,12,22]
##print(list_a)
##for i in range(len(l)):
##    for j in range(i+1,len(l)):
##        if l[i]>l[j]:
##            l[i],l[j]=l[j],l[i]
##print(l)
##    
def sort(a):
    n=len(a)
    for i in range(n):
         for j in range(0,n-i-1):
             if a[j]>a[j+1]:
                 a[j],a[j+1]=a[j+1], a[j]
a=[2,5,12,6,1,4]
sort(a)
print("Sorted array is:")
for i in range(len(a)):
    print(a[i], end=" ")
