##4.wap that take a two two strings from input and return the combination of the two string characters like below:
##input:
##string1="harry"
##string2="micheal"
##output:
##['hm','ai','rc','rh','ae','ya','l']
def merge(a,b):
    res=""
    i=0
    while (i<len(a)) or (i<len(b)):
        if (i<len(a)):
            res+=a[i]
        if (i<len(b)):
            res+=b[i]+","
        i+=1
    return res
a="harry"
b="micheal"
print(merge(a,b))
