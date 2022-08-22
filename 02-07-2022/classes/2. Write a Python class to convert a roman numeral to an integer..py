##2. Write a Python class to convert a roman numeral to an integer.
class Integerroman:
    def roman_to_int(self,num):
        romans={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        int_val=0
        for i in range(len(num)):
            if i>0 and romans[num[i]]>romans[num[i-1]]:
                int_val+=romans[num[i]]-2*romans[num[i-1]]
            else:
                int_val+=romans[num[i]]
        return int_val
print(Integerroman().roman_to_int("C"))
print(Integerroman().roman_to_int("CD"))
        
        
