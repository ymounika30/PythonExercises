##3). wap solve this pattern
##
##  5 5 5 5 5
##   * * * *
##    3 3 3 
##     * *
##      1
a=int(input())
for i in range(a,0,-1):
    for j in range(a,0,-1):
        if i>=j:
            if i%2==0:
                print("*",end=" ")
            else:
                print(i,end=" ")
        else:
            print('',end=" ")
    print()
