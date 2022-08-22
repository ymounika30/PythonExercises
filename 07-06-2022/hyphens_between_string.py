#Join a list of strings into a single string, delimited by hyphensa
a=input()
b=""
for i in a:
    b=b+i+"-"
    x=b.strip("-")
print(x)
            
