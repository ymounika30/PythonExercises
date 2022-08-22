'''1) write a python program on files to check whether the given file exists or not. 
if it is available then print its content? '''
##import os
##fileexits=os.path.isfile("story1.txt")
##print(fileexits)
##f=open("story1.txt","r")
##f.read()
##f=open("story1.txt","r+")
##f.write("Mounika learns Python")
##d=f.read()
##print(d)
##f.close()
##==============================================================================================================================================
'''2) Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.'''
##import string
##def alphabets_file(a):
##    with open("story.txt","w") as f:
##        alphabet=string.ascii_uppercase
##        letters=[alphabet[i:i+a]+"\n" for i in range(0,len(alphabet),a)]
##        f.writelines(letters)
##alphabets_file(3)

##==============================================================================================================================================
'''3) Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt'''
##import string, os
##if not os.path.exists("letters"):
##   os.makedirs("letters")
##for letter in string.ascii_uppercase:
##   with open(letter + ".txt", "w") as f:
##       f.writelines(letter)

##==============================================================================================================================================
'''4) Write a Python program to interleave multiple lists of the same length. Use itertools module. '''
##import itertools
##def interleave_multple_lists(l1,l2,l3):
##    res=list(itertools.chain(*zip(l1,l2,l3)))
##    return res
##l1=[1,2,3,4,5,6,7,8,9]
##l2=[11,12,13,14,15,16,17,18,19]
##l3=[21,22,23,24,25,26,27,28,29]
##print(interleave_multple_lists(l1,l2,l3))
##==============================================================================================================================================
'''5) Using lambda function print following output.
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz
'''

##x=list( map ( lambda i: 'FizzBuzz' if i%15 == 0 else 'Fizz' if i%3 == 0 else 'Buzz' if i%5 == 0  else i , [ i for i in range(1,31) ] ) )
##for i in x:
##    print(i)

