##1write a program to print the list of elements of prinicipal diaognal
##input:
##3 3
##1  2 3
##10 20 30
##5  10 15
##output:[1, 20, 15]
def prinicipal_diagonal(matrix):
    list1=[]
    c=0
    for i in matrix:
        if c<b:
            list1+=[i[c]]
            c=c+1
    print(list1)
def conv_str_to_int(lista):
    list2=[]
    for i in lista:
        list2+=[int(i)]
    return list2
a,b=input().split()
a,b=int(a),int(b)
numlist=[]
for i in range(a):
    lista=input().split()
    lista=conv_str_to_int(lista)
    numlist+=[lista]
prinicipal_diagonal(numlist)
            
