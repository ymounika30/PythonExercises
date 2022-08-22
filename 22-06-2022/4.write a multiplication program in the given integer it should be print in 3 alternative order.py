##4.write a multiplication program in the given integer it should be print in 3 alternative order
##input:3
##output:3x1=3
##       3x3=9
##       3x5=15
a=int(input())
for i in range(1,7,2):
        print(str(a)+"x"+str(i)+"="+str(a*i))
        
