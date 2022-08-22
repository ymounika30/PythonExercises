## 1.Write a Python class to convert an integer to a roman numeral
class Roman:
    def int_to_roman(self,num):
        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman_num=''
        i=0
        while num>0:
            for k in range(num//val[i]):
                roman_num+=romans[i]
                num-=val[i]
            i+=1
        return roman_num
print(Roman().int_to_roman(100))
print(Roman().int_to_roman(400))
