##2.write a python program to implement matrix multiplication.

a=[[1,2,3],[5,3,2],[7,9,8]]
b=[[3],[3],[3]]
len_a=len(a)
len_b=len(b)
index_a=len(a[0])
index_b=len(b[0])
if index_a!=len_b:
    print("error")
    quit()
l=[]
for row in range(len_a):
    c_row=[]
    for col in range(index_b):
        c_row.append(0)
    l.append(c_row)

for i in range(len_a):
    for j in range(index_b):
        c_value=0
        for k in range(index_a):
            c_value+=a[i][k]*b[k][j]
        l[i][j]=c_value
print(l)

