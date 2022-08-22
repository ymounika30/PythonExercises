##4. Roman Numerals
##Write a program to convert a non-negative integer N to its Roman numeral representation. Roman numerals are usually written
##largest to smallest from left to right.
##symbol value
##I 1
##V 5
##X 10
##L 50
##C 100
##D 500
##M 1000
##A number containing several decimal digits is built by appending Roman numeral equivalent for each, from highest to lowest, as in the following examples:
##39 = XXX + IX = XXXIX.
##246 = CC + XL + VI = CCXLVI.
##789 = DCC + LXXX + IX = DCCLXXXIX.
##2,421 = MM + CD + XX + I = MMCDXXI.
##160 = C + LX = CLX
##207 = CC + VII = CCVII
##1,009 = M + IX = MIX
##1,066 = M + LX + VI = MLXVI
##1776 = M + DCC + LXX + VI = MDCCLXXVI
##1918 = M + CM + X + VIII = MCMXVIII
##Sample Input 1
##2
##Sample Output 1
##II
##Sample Input 2
##1994
##Sample Output 2
##MCMXCIV 
a=int(input())
num=[1,5,10,50,100,500,1000]
rom=["I","V","X","L","C","D","M"]
i=6
while a>0:
    divided=a//num[i]
    a=a%num[i]
    while divided>0:
        print(rom[i], end="")
        divided=divided-1
    i=i-1
