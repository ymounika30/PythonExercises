#How would you check if each word in a string begins with a capital letter?

a=input()
for i in a:
    if i[0].istitle():
        print(i)
        
