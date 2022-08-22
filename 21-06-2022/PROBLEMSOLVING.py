##given integer n as input, write a program to display the sum of the first n terms in harmonic series.
##
##The series is:1+1/2+1/3+1/4+1/5+......+1/N (N terms)
##
##input:
##      The first line of input is an integer N
##
##output:
##      print the sum rounded upto 2 decimal places
##explanation:
##      for n=5
##      the sum of first 5 terms in harmonic series 1+1/2+1/3+1/4+1/5
##      so, the output should be 2.28
##sample input1: 5
##sample output1: 2.28
##sample input2: 3
##sample output2: 1.83
a=int(input())
b=0
for i in range(1,a+1):
    x=1/i
    b=b+x
print(round(b,2))
