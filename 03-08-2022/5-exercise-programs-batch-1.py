'''1).Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
##a=[]
##b=[i for i in input().split(",")]
##for x in b:
##    i=int(x,2)
##    if  i%5==0:
##        a.append(x)
##print(",".join(a))

##===================================================================================================================================
'''2).Write a menu driven program which shows all operations on Binary File 
Add Record 
Display All Record 
Display Specific Record 
Modify Record 
Delete Record 
Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type
'''
##import pickle
##import os
##def main_menu():
##    print("1. Add a new record")
##    print("2. Display all record")
##    print("3. Display Specific record")
##    print("4. Modify a record")
##    print("5. Delete a record")
##    print("6. Exit")
##    ch = int(input("Enter your choice:"))
##    if ch==1:
##        addrec()
##    elif ch==2:
##        disp()
##    elif ch==3:
##        
##        specific_rec()
##    elif ch==4:
##        mod()
##    elif ch==5:
##        del()
##    elif ch==6:
##        print("Bye")
##    else:
##        print("Invalid Choice.")
##def addrec():
##     L=[ ]
##     f=open("data.dat","ab")
##     rn = int(input("Enter Room Number"))
##     pr = int(input("Enter the price of room"))
##     rt = input("Enter the type of room")
##     L  = [rn, pr, rt]
##     pickle.dump(L, f)
##     print("Record added in the file")
##     f.close()
##
##def disp():
##  try:
##      f=open("data.dat","rb")
##      while True:
##            d=pickle.load(f)
##            print(d)
##  except:
##      f.close()
##
##def specific_rec():
##  rno=int(input("Enter Room number to search"))
##  try:
##    f1=open("data.dat","rb")
##    while True:
##      d=pickle.load(f1)
##      if rno==d[0]:
##          print(d)
##  except:
##    f1.close()
##    
##def mod():
##  roll = int(input("Enter room number whose record you want to Modify:"))
##  try:
##      file = open("data.dat","rb+")
##      f=open("temp1.dat","wb")
##      
##      while True:
##          d = pickle.load(file)
##          if roll == d[0]:
##              d[1]=int(input("Enter modified price"))
##              d[2]=input("Enter modified room type")
##          pickle.dump(d,f)
##  except:
##      print("Record Updated")
##      file.close()
##      f.close()
##      os.remove("data.dat")
##      os.rename("temp1.dat","data.dat")
##
##def delete():
##  roll = int(input("Enter room number whose record you want to delete:"))
##  try:
##      file = open("data.dat","rb+")
##      f=open("temp1.dat","wb")
##      while True:
##          d = pickle.load(file)
##          if roll != d[0]:
##              pickle.dump(d,f)
##  except:
##      print("Record Deleted")
##      file.close()
##      f.close()
##      os.remove("data.dat")
##      os.rename("temp1.dat","data.dat")
##===================================================================================================================================
'''3).Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat”
whoose model number (integer type) is passed as an argument.
Structure of “mobile.dat” is [Mobile id, Mobile brand, Model No., Price]'''
##mobileid = [220,224,112,445,667]
##mobilebrand = ['vivo','realme','redmi','windows','mi']
##modelno = [1,2,3,4,5]
##price = [100,200,300,2000,4500]
##with open('mobile.dat','w') as f:
##    for i in range(5):
##        lst = f'{mobileid[i]},{mobilebrand[i]},{modelno[i]},{price[i]}\n'
##        f.write(lst)
##        
##def foo(n):
##    with open('mobile.dat','r') as f:
##        for i in f.readlines():
##            lst = i.split(',')
##            if lst[2]==n:
##                print(lst)
##
##foo('5')
##===================================================================================================================================
'''4).Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and
the values are square of keys.'''
##def disp(a):
##    dict1=dict()
##    for i in range(a):
##        dict1[i]=a**2
##    print(dict1)
##disp(2)
##===================================================================================================================================
'''
5).Please write a program using generator to print the numbers which can be
divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
'''
##def div(a):
##    for i in range(a):
##        if i%5==0 and i%7==0:
##            yield(i)
##for i in div(200):
##    print(i)
        
