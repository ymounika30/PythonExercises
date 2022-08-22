#Check if a string contains only numbers
a=input()
b=""
for i in a:
    if i.isdigit():
        b=b+i
print(b)
        
