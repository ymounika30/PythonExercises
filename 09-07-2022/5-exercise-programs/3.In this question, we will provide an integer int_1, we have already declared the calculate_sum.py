##3.In this question, we will provide an integer int_1, we have already declared the calculate_sum 
##function for you in solution.py. The initial int_1 of this function represents the initial value, 
##and you need to calculate the form a + aa + aaa + aaaa value, and finally print the result.
##input:5
##output:6170
a=int(input())
b=0
c=0
for i in range(1,a):
    b=b*10+a
    c=c+b
print(c)
