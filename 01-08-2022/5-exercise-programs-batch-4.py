'''1.write a python program do multiplication program using generators and use sys module to find memory size'''
##import sys
##def multiplication(a):
##    for i in range(1,a+1):
##        yield a*i
##for i in (multiplication(5)):
##    print(i)
##a = sys.getsizeof(i)
##print(a)
##======================================================================================================================================================
'''2..write a python program do multiplication program using function'''
##def multiplication(a):
##    for i in range(1,a+1):
##        print(a*i)
##a=int(input())
##multiplication(a)

##========================================================================================================================================================
'''3.Write a Python program to extract characters from various text files and puts them into a list.'''
##import glob
##b=[]
##c=glob.glob("poem.txt")
##for i in c:
##    with open(i,"r") as f:
##        b.append(f.read())
##print(b)
##============================================================================================================================================================
'''4. Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.'''
import string
def alphabets_file(a):
    with open("poem.txt","w") as f:
        alphabet=string.ascii_uppercase
        letters=[alphabet[i:i+a]+"\n" for i in range(0,len(alphabet),a)]
        f.writelines(letters)
alphabets_file(3)
##============================================================================================================================================================
'''5.write a python program in twin prime using outer and inner functions'''
##def outer(a):
##    def inner():
##        x=int(input())
##        for i in range(2,x):
##            f=0
##            for j in range(2,i):
##                if (i%j)==0:
##                    f=f+1
##            if f==0:
##                p=i+2
##                c=0
##                for k in range(2,p):
##                    if (p%k)==0:
##                        c=c+1
##                if c==0:
##                    print(i,p)
##    return inner
##def new():
##    pass
##res=outer(new)
##res()
