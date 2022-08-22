##1.Write a Python program to convert string element to integer inside a given tuple using lambda.
##input tuple values:
##(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
##output tuple values:
##((233, 33), (1416, 55), (2345, 34))
def tuple_int_str(a):
    result=tuple(map(lambda x: (int(x[0]),int(x[2])),a))
    return result
a=("233","ABCD","33"),("1416","EFGH","55"),("2345","WERT","34")
print(tuple_int_str(a))
