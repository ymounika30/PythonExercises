'''1) take a list and output has to be repeated of the second half of the list elements
input = [1,2,3,4,5,6]
output = [4,5,6,4,5,6]'''
##a=[1,2,3,4,5,6]
##n=len(a)//2
##print(a[n:]*2)

##==================================================================================================================================================================
'''2) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)'''
##a=input()
##if ord(a)>=97 and ord(a)<=123:
##    print("True")
##elif ord(a)>=65 and ord(a)<=91:
##    print("True")
##elif ord(a)>=48 and ord(a)<=57:
##    print("True")
##else:
##    print("False")
##==================================================================================================================================================================
'''3) Write a Python program that matches a string that has an a followed by zero or more b's'''
##a=input()
##if a[0]=="a" and a[1:]=="b":
##    print("True")
##else:
##    print("False")
##==================================================================================================================================================================
'''4) Write a Python program that matches a word at the beginning of a string'''
##a=input()
##a.startswith("Mounika")
##print(a)
##==================================================================================================================================================================
'''5) open a file and enter a lists like each list is having two or more elements in to the file and retrieve their details in the ouput in lists'''
##places_list = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
##with open('data.txt', 'w') as f:
##    f.writelines("%s\n" % place for place in places_list)
