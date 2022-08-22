##2). wap take one example wrong method overloding
class A:
    def disp(z,x):
        print(z+x)
        print("Im a in 1 add")
    def disp(a,b,c):
        print(a+b+c)
        print("Im in 2nd add")
a=A.disp(10,20,30)
A.disp(10,50)
