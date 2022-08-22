##5.Mathematicians have come up with a famous conjecture - the Collatz conjecture.
##For any positive integer n, if n is even, make it n // 2.
##If n is an odd number, make it 3 * n + 1.
##If you follow this rule, you must end up with 1.
##How many rounds of transformation will that number go through to become 1?
def collatz(num):
    while num!=1:
        print(num)
        if num%2==0:
            num=int(num/2)
        else:
            num=int(3 * num + 1)
    else:
        print(num)
        print("Done!")
def disp():
    num=int(input())
    collatz(num)
disp()
