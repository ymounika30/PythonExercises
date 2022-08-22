##3. 	 a. Write a python program to find the power of a number using recursion
'''
def power(a,b):
    if b==0:
        return 1
    else:
        msg=a*power(a,b-1)
    return msg
a=2
b=3
print(power(a,b))
'''
##Output:8






##b. Write a Python program of recursion list sum 
##Test Data: [1, 2, [3,4], [5,6]]
##Expected Result: 21
def sum_list(a):
    b=0
    for i in a:
        if type(i)==type([]):
            b=b+sum_list(i)
        else:
            b=b+i
    return b
print(sum_list([1, 2, [3,4], [5,6]]))

##Output:21
