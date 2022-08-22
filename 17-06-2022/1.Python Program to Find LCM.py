z=["sravani","tommy","jerry","timmy"]
c=''
for i in range (len(z)):
    if i%2!=0:
        c=c+z[i][::-1]+' '
    else:
        c=c+z[i]+' '
    
print(c)


