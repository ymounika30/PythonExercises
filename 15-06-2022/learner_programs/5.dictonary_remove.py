##5 write a program to remove n key-value pairs from the dictionary if they present
b={
    "name":"mounika",
    "software":"python"
}

a=input().split()
for i in a:
    if i in b:
        del b[i]
print(b)
