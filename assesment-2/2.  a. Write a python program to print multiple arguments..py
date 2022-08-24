##2.  	a. Write a python program to print multiple arguments.
'''
def pos(*a):
    print(a)
a=("mounika","priya","usha")
pos(a)
'''
##
##Output:
##(('mounika', 'priya', 'usha'),)







##	b. Write a function that accepts variable length key value pair as arguments.
'''
def key(**a):
    return a
print(key(key_1="Mounika",key_2="Usha",key_3="priya"))
'''
##Output:
##{'key_1': 'Mounika', 'key_2': 'Usha', 'key_3': 'priya'}
