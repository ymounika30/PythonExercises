'''a = 10
b = 0
try:
    d = a/b
    print(d)
    print('Inside Try')
except ZeroDivisionError:
    print('Division by Zero Not allowed')
print('Rest of the Code')'''
##=========================================================================================================================================
'''a = 10
b = 0
try:
    d = a/b
    print(d)
    print('Inside Try')
except ZeroDivisionError:
    print('Division by Zero Not allowed')
else:
    print('Inside Else')
print('Rest of the Code')    
'''
##=========================================================================================================================================
'''
a = 10
b = 9
try:
    d = a/b
    print(d)
    print('Inside Try')
except ZeroDivisionError:
    print('Division by Zero Not allowed')
else:
    print('Inside Else')
finally:
    print('Inside Finally')
print('Rest of the Code')
'''
##=========================================================================================================================================
'''
a = 10
b = 0
try:
    d = a/b
    print(d)
    print('Inside Try')
except ZeroDivisionError as obj:
    print(obj)
print('Rest of the Code')
'''
##=================================================================================================================================================
'''
a = 10
b = 9
try:
    d = a/o
    print(d)
except ZeroDivisionError as obj:
    print(obj)
except NameError as ob:
    print(ob)
print('Rest of the Code')
'''
##=================================================================================================================================================
'''
a = 10
b = 0
try:
    d = a/g
    print(d)
except (NameError, ZeroDivisionError) as obj:
    print(obj)
print('Rest of the Code')
'''
##=====================================================================================================================================================
'''
a = 10
b = 0
try:
    d = a/b
    print(d)
except:
    print('Exception Handler')
print('Rest of the Code')
'''
##=======================================================================================================================================================
'''
a=10
assert a<=5, "Invalid Number"
'''
##==============================================================================================================================================================
'''
class BalanceException (Exception):
    #pass
    def __init__(self, arg):
        self.msg = arg
def checkbalance():
    money = 10000
    withdraw = 9000
    try:
        balance = money - withdraw
        if(balance<=2000):
            raise BalanceException('Insufficient Balance')
        print(balance)
    except BalanceException as be:
        print(be)
        
checkbalance() 
'''
