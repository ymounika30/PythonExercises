##10. Create an inner function to calculate the addition in the following way
##Create an outer function that will accept two parameters a and b
##Create an inner function inside an outer function that will calculate the addition of a and b
##At last, an outer function will add 5 into addition and return it.
def outer_fun(a, b):
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5
a=int(input())
b=int(input())
result = outer_fun(a,b)
print(result)
