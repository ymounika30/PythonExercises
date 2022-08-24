##33.  Write a Python program to add two given lists using map and lambda. 
## Original list:
##[1, 2, 3]
##[4, 5, 6]
##Result: after adding two list
##[5, 7, 9]
a=input().split()
b=input().split()
list1=[]
list2=[]
list3=[]
for i in a:
    list1+=[int(i)]
for j in b:
    list2+=[int(j)]
x=list1[0]+list2[0]
y=list1[1]+list2[1]
z=list1[2]+list2[2]
print(x,y,z)

Input:1 2 3
      4 5 6
Output: 5 7 9

