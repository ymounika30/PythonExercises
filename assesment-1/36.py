##36. Write a Python program to check if two given sets have no elements in common
x = {1,2,3,4}
y = {4,5,6,7}
z = {8}
print(x)
print(y)
print(z)
print("Compare x and y:")
print(x.isdisjoint(y))
print("Compare x and z:")
print(z.isdisjoint(x))
print("Compare y and z:")
print(y.isdisjoint(z))


##Output:
##{1, 2, 3, 4}
##{4, 5, 6, 7}
##{8}
##Compare x and y:
##False
##Compare x and z:
##True
##Compare y and z:
##True
