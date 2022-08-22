##7.Write a Python class to implement pow(x, n).
class Power:
    def pow(self,a,b):
        if a==0 or a==1 or b==1:
            return a
        if a==-1:
            if b%2==0:
                return 1
            else:
                return -1
        if b==0:
            return 1
        if b<0:
            return 1/self.pow(a,-b)
        val=self.pow(a,b//2)
        if b%2==0:
            return val*val
        return val*val*a
print(Power().pow(3,5))
        
