##11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
##Example:
##0100,0011,1010,1001
##Then the output should be:
##1010
##Notes: Assume the data is input by console.
def my_fun(bina):
    for binary in bina:
        bin2=binary[::-1]
        k=0
        digit=0
        for i in bin2:
            twos=2**k
            k=k+1
            if i=="1":
                digit=digit+twos
        if digit%5==0:
            print(binary)
binary=["0100","0011","1010","1001"]
my_fun(binary)
