##3) Find the digit is binary or not?
##eg:-1011
##is binary number
a=int(input())
b=""
x=a
while (x>0):
    k=x%2
    b=str(k)+b
    x=int(x/2)
if b:
    print(str(b)+"is a binary number")
else:
    print("Not a binary Number")
