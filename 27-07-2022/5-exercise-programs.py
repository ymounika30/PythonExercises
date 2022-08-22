'''1.write a python program in shutil module using copy method'''

##import shutil
##source=r"C:\Users\my22114\Documents\pythonexercises\27-07-2022\story.txt"
##destination=r"C:\Users\my22114\Documents\pythonexercises\27-07-2022\task.txt"
##shutil.copyfile(source,destination)

##===============================================================================
'''2.write a pthon program in os module using rename method'''
##
##import os
##source=r"C:\Users\my22114\Documents\pythonexercises\27-07-2022\story.txt"
##destination=r"C:\Users\my22114\Documents\pythonexercises\27-07-2022\story1.txt"
##os.rename(source,destination)

##===============================================================================
'''3.write a python program in fibonacci series using outer and inner functions'''
##def outer(n):
##    def inner():
##        x=int(input())
##        a=0
##        b=1
##        for i in range(1,x+1):
##            c=a+b
##            a=b
##            b=c
##            print(c)
##    return inner
##def new():
##    pass
##res=outer(new)
##res()

##===============================================================================
'''4.write a python program in heapq module'''
##import heapq
##l1=[5,7,9,1,3]
##heapq.heapify(l1)
##print(list(l1))
##heapq.heappush(l1,4)
##print(list(l1))
##print(heapq.heappop(l1))

##==============================================================================
'''5.write a python program in shallow copy and deep copy'''
##import copy
##l1=[[1,2,3],[4,5,6]]
##l2=copy.deepcopy(l1)
##print(l2)
##l2[1][1]=6
##print(l2)
##
##l3=[1,2,3,4,5,6]
##l4=l3.copy()
##print(l4)
##l4[4]=3
##print(l4)
