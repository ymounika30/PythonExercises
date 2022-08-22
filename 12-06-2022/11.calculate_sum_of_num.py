##11.Write a recursive function to calculate the sum of numbers from 0 to 10
def calc_sum_numbers(a):
    b=0
    for i in range(1,a+1):
        b=b+i
    return b
a=int(input())
print(calc_sum_numbers(a))
