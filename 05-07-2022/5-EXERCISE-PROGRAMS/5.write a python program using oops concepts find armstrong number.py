##5.write a python program using oops concepts find armstrong number
class Armstrong:
    def __init__(self,a):
        self.a=a
    def is_arm_strong(self):
        sum=0
        b=len(self.a)
        for i in a:
            c=int(i)
            sum=sum+(c**b)
        x=int(self.a)
        if sum==x:
            print("Armstrong")
        else:
            print("Not Armstrong")
a=input()
check_armstrong=Armstrong(a)
check_armstrong.is_arm_strong()
