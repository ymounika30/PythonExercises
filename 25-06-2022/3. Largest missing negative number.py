##3. Largest missing negative number 
##you are given unsorted array A of N integers . you have to find the largest negative integer missing from the array.
##example:1
##input: A = -2 -1 0 1 2 
##output:-3
##example2:
##input:-11 -10 -12
##output:-1  
a=input().split()
b=-1
for i in a:
    if b not in a:
        print(b)
        break
    else:
        b=b-1
