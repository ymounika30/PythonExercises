'''1.write a python program on logging'''
##import logging
##logging.basicConfig(filename='student.log',
##                     level=logging.INFO,
##                     format='%(lineno)s::%(asctime)s::%(levelname)s::%(message)s::%(name)s')
##logger = logging.getLogger('Mounika')
##def validation(fun):
##    logger.info("Enter validation function")
##    def fun(userinput):
##        logger.info("Before Checking in Data")
##        data=["Mounika"]
##        if userinput in data:
##            logger.info("username present in database")
##            return "welcome ",userinput
##        else:
##            logger.info("username Not present in database")
##            return "wrong user"
##    return fun
##@validation
##def login_user(userinput):
##    return userinput
##userinput=input()
##logger.info("User Input given")
##==================================================================================================================================================================================
'''2.write a python program to remove all the occurances of the given number'''
##a=[5,10,20,30,40,5,100,200,10,500,1000]
##b=int(input())
##x=a.count(b)
##for i in range(x):
##    a.remove(b)
##print(a)
##==================================================================================================================================================================================
'''3.write a python program to exact the numbers in a given string and print sum,minimum and maximum of those numbers'''
##a=input()
##c=[]
##for i in a:
##    if i.isdigit():
##        c+=[int(i)]
##print(sum(c))
##print(min(c))
##print(max(c))

##==================================================================================================================================================================================
'''4.write a python program on sprial number 
eg:-9 8 7     
    2 1 6        
    3 4 5'''
##x=1
##p=[9,8,7,6,5,4,3,2,1]
##q=[1,2,3,4,5,6,7,8,9]
##for i in p:
##    q[i-1]=x
##    x+=1
##y=0
##for i in p:
##    print(i, end=" ")
##    y+=1
##    if y%3==0:
##        print()

##==================================================================================================================================================================================
'''5.create a list of combinations of entered number like below
input: 5
list must be created as [4,4,4,33,33,22,22,1,1,1]'''
##
##a=int(input())
##b=[]
##for i in range(a-1,0,-1):
##    if i==1 or i==a-1:
##        b.append(i)
##        b.append(i)
##        b.append(i)
##    else:
##        b.append(str(i)*2)
##        b.append(str(i)*2)
##print(b)
