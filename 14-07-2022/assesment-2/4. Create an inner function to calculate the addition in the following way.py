##4. Create an inner function to calculate the addition in the following way
##Create an outer function that will accept two parameters, a and b
##Create an inner function inside an outer function that will calculate the addition of a and b
##At last, an outer function will add 5 into addition and return it
def outer(a,b):
    sum=0
    def inner():
        sum=a+b
        return sum
    return inner()+5
a=10
b=20
print(outer(a,b))

##Output:35
