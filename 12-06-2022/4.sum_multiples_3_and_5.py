##4.Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def multiply_sum_3_and_5(a):
    b=0
    for i in range(1,a+1):
        if (i%5)==0 or (i%3)==0:
           b=b+i
    print(b)
        
a=int(input())
multiply_sum_3_and_5(a)
