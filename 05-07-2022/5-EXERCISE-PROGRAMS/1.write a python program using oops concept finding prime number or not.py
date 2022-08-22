##1.write a python program using oops concept finding prime number or not
class Check:
    def __init__(self,num):
        self.num=num
    def isPrime(self):
        for i in range(2,num):
            if (num%i)==0:
                return False
        return True
num=12
check_prime=Check(num)
print(check_prime.isPrime())
