##write a python program on sprial number using inner function
##and decorator
##eg:-1 2 3
##    8 9 4
##    7 6 5

def outer(a):
    def inner():
        x=1
        p=[1,2,3,4,5,16,17,18,19,6,15,24,25,20,7,14,23,22,21,8,13,12,11,10,9]
        q=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        for i in p:
            q[i-1]=x
            x+=1
        y=0
        for i in p:
            print(i, end=" ")
            y+=1
            if y%5==0:
                print()
    return inner
@outer
def new():
    pass
new()



