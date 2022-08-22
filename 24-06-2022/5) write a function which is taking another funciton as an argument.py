##5) write a function which is taking another funciton as an argument
def fibonacci(a):
    if a<=1:
        return a
    else:
        msg=fibonacci(a-2)+fibonacci(a-1)
    return msg
def fibonacciseries(a):
    list_a=[]
    for i in range(a):
        list_a+=[fibonacci(i)]
    return list_a
a=int(input())
print(fibonacciseries(a))
