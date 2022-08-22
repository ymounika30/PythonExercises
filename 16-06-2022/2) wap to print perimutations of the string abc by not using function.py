#2) wap to print perimutations of the string "abc" by not using function.'''
string="abc"
for i in string:
    for j in string:
        for k in string:
            if i!= j and i!=k and j!=k:
                print(i,j,k)
