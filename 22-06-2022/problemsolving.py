##Sam has purchased N boxes of fruits. Each box i contains Fi number of fruits. 
##Sam wants to store all the fruits in a single box.But he cannot move fruits
##from one box to a box that already contains some fruits.He can choose any
##two boxes and move their combined contents to a new empty box.
##
##If the boxes selected for transferring fruits, contain X and Y number of fruits
##respectively, then it takes him exactly X+Y seconds to transfer fruits to a new box.
##
##Input:
##
##The first line of input is the number of test case T
##Each test case is comprised of two lines.
##The first line of the test case is the number of boxes N.
##The second line of the test cases is N space-seperated integers 
##denoting the number of fruits in each box.
##
##Output:
##Print the minimum time required, in seconds,for each of the test cases
##in a new line.
##
##Explation:
##Given T=1
##n=4 and F=10 2 3 4
##Each of these 4 boxes contains fruits as mentioned below:
##B1=10 fruits
##B2=2 fruits
##B3= 3 fruits
##B4= 4 fruits
##
##Move fruits from boxes B2 and B3 to new box B5.
##Time taken =>2+3=5 seconds. B5 now contains 5 fruits.
##
##Move fruits from boxes B4 and B5 to new box B6.
##Time taken => 4+5=9 seconds. B6 now contains 9 fruits.
##
##Move fruits from boxes B6 and B1 to a new box B7.
##Time taken => 9+10=19 seconds.B7 now contains all of the fruirts.
##
##=>Total time taken=5+9+19=33
##
##So the output is 33
##
##Sample Input 1:
##No of boxes:4
##10 2 3 4
##Sample output 1:
##33
##
##Sample Input 1:
##No of boxes:5
##1 2 3 4 5
##Sample output 1:
##14
boxes=int(input())
b=[]
p=[]
x=0
y=0
for i in range(boxes):
    a=int(input())
    b.append(a)
c=sorted(b)
for i in c:
    x=x+i
    print(x)
    p+=[x]
    print(p)
for i in p:
    y=y+i
print(y-p[0])

