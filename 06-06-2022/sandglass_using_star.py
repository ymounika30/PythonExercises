a=int(input())
for i in range(1,a+1):
    first=" "*(i-1)
    row=a-(i-1)
    space=""
    for j in range(1,row+1):
        space=space+("* "+" ")
    print(first+space)
for i in range(1,a+1):
    space=" "*(a-i)
    stars=""
    for j in range(1,i+1):
        stars=stars+("* "+" ")
    print(space+stars)
l
