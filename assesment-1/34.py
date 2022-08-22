##34. Write a Python program to select a random element from a list, set, dictionary (value) and a file from a directory. Use random.choice()
import random
a=[1, 2, 3, 4, 5]
print("Select a random element from a list:")
print(random.choice(a))
print(random.choice(a))
print(random.choice(a))
b=set([1, 2, 3, 4, 5])
print("\nSelect a random element from a set:")
print(random.choice(tuple(b)))
print(random.choice(tuple(b)))
print(random.choice(tuple(b)))
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("\nSelect a random value from a dictionary:")
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key]) 


##Output:
##Select a random element from a list:
##4
##1
##2
##
##Select a random element from a set:
##4
##1
##3
##
##Select a random value from a dictionary:
##3
##5
##5
