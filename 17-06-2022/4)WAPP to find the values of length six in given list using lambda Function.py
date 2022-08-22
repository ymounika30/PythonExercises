 #4)WAPP to find the values of length six in given list using lambda Function.'''
z=["sravani","sraani","sravni","sravani"]
a=filter(lambda x:x if len(x)==6 else "",z)
for i in a:
    print(i)
