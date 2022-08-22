##4.write a program Russian Multiplication using class and object
class Mult:
    def russian(self,a,b):
        res=0
        while b>0:
            if b&1:
                res=res+a
            a=a<<1
            b=b>>1
        return res
obj=Mult()
print(obj.russian(4,5))
                                                            
                
