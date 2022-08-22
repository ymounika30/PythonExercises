##2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
##( Iterate over list using while loop ).
a=10
b=[]
c=[]
i=0
while i<10:
    x=int(input())
    b+=[x]
    i+=1
print(b)
c=int(input())
if c in b:
    print("True")
else:
    print("No")
