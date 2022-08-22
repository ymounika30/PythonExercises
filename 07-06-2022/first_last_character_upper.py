#Uppercase first and last character of a string
a=input()
n=len(a)
x=a[0].upper()
y=a[n-1].upper()
print(x+a[1:n-1]+y)
