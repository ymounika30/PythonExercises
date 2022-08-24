##1.Write a program in python to replace all word “the” by another word “them” in a file “poem.txt”. 
'''
f=open("poem.txt","r")
d=f.read()
d=d.replace("the","them")
f.close()
f=open("poem.txt","w")
f.write(d)
f.close()
'''

##=========================================================================================================================================================================

##2.Write a program in python to replace a character by another character in a file “story.txt”. (Accept both the characters from the user)
'''
f=open("story.txt","r")
d=f.read()
a=input()
b=input()
d=d.replace(a,b)
f.close()
f=open("story.txt","w")
f.write(d)
f.close()
'''
##=========================================================================================================================================================================
##3.Write a program in python to replace all the ‘a’ by ‘@’ in a file “data.txt”.
'''
f=open("data.txt","r")
d=f.read()
d=d.replace("a","@")
f.close()
f=open("data.txt","w")
f.write(d)
f.close()
'''
##=========================================================================================================================================================================
##4.Write a program in python to read file “data.txt” and display only those lines whose length is more than 40 characters.
'''
f=open("data.txt","r")
d=f.readlines()
for i in d:
    if len(i)>40:
        print(i)
'''
##=========================================================================================================================================================================
##5.Write a program in python to remove all duplicate lines from the file “story.txt”.
'''
f=open("story.txt","r")
d=f.readlines()
for i in d:
    x=[]
    if i not in x:
        x.append(i)
    print(x)
f.close()
f=open("story.txt","w")
for i in x:
    f.write(i)
f.close()
'''
##=========================================================================================================================================================================
##6.Write a program in python to display only unique words from the file “story.txt”.
'''
f=open("story.txt","r")
d=f.read()
d=d.split()
b=""
for i in d:
    if i not in b:
        b=b+i
print(b)
f.close()
'''
##=========================================================================================================================================================================
##7.Write a program in python to count the frequency of each vowels in a file “task.txt”.
'''
f = open("task.txt", "r")
d = f.read()
va=ve=vo=vu=vi=0
for i in d:
     if i=='a' or i=='A':
         va=va+1
     if i=='e' or i=='E':
         ve=ve+1
     if i=='i' or i=='I':
         vi=vi+1
     if i=='o' or i=='O':
         vo=vo+1
     if i=='u' or i=='U':
         vu=vu+1
print("Frequency of vowel \"a\" is", va)
print("Frequency of vowel \"e\" is", ve)
print("Frequency of vowel \"i\" is", vi)
print("Frequency of vowel \"o\" is", vo)
print("Frequency of vowel \"u\" is", vu)
'''
##=========================================================================================================================================================================
##8.Write a program in python to count those words whose length is more than 7 characters in a file “story.txt”.
'''
f=open("story.txt", "r")
d=f.read()
d=d.split()
c=0
for i in d:
  if len(i)>7:
    c=c+1
print("Total words are :", c)
'''
##=========================================================================================================================================================================
##9.Write a program in python to count those lines from the file “div.txt” which are starting from ‘T’ or ‘M’.
'''
f=open("div.txt", "r")
d=f.readlines()
c=0
for i in d:
     if i[0] == 'M' or i[0] == 'T':
        c=c+1
print("Total lines are :", c)
'''
##=========================================================================================================================================================================
##10.Write a program in python to count those lines from the file “div.txt” which are not starting from ‘M’.
'''
f=open("div.txt")
d=f.readlines()
c=0
for i in d:
     if i[0] != 'M':
         c=c+1
print("Total lines are :", c)
'''
##=========================================================================================================================================================================
##11.Write a program in python to display those words from a file “image.txt” which are ending from alphabet ‘m’.
'''
f=open("image.txt")
d=f.read()
d=d.split()
c=0
for i in d:
    if i[-1]=='m':
        c=c+1
print("Total words are :", c)
'''
##=========================================================================================================================================================================
##12.Write a program in python to read all lines of file “data.txt” using readline() only.
'''
f=open("data.txt", "r")
str = " "
while str:
     str = f.readline()
     print(str, end = "")
f.close()
'''
##=========================================================================================================================================================================
##13.Write a program in Python to copy the entire content from file “data.txt” to “story.txt”
'''
f = open("data.txt", "r")
f1 = open("story.txt", "w")
d = f.read()
f1.write(d)
f.close()
f1.close()
'''
##=========================================================================================================================================================================
##14.Write a program in Python to copy the alternate lines from file “data.txt” to “story.txt
'''
f = open("data.txt", "r")
f1 = open("story.txt", "w")
d = f.readlines()
for i in range(len(d)):
    if i%2==0:
       f1.write(d[i])
f.close()
f1.close()
'''
##=========================================================================================================================================================================
##15.Write a program in Python to read the entire content from file “data.txt” and copy the contents to “story.txt” in upper case.
'''
f = open("data.txt", "r")
f1 = open("story.txt", "w")
d = f.readlines()
for i in d:
    f1.write(i.upper())
f.close()
f1.close()
'''
##=========================================================================================================================================================================
##16.Write a program in Python to read the entire content from file “data.txt” and copy only those words to “story.txt” which start from vowels.
'''
f = open("data.txt", "r")
f1 = open("story.txt", "w")
d = f.read()
d = d.lower()
word = d.split()
for i in word:
    if  i[0] in ['a', 'e', 'i', 'o', 'u']:
        f1.write(i)
f.close()
f1.close()
'''
##=========================================================================================================================================================================
##17.Write a program in Python to read the entire content from file “data.txt” and copy only those words in separate lines to “story.txt” which are starting from lower case alphabets .
'''
f = open("data.txt", "r")
f1 = open("story.txt", "w")
d = f.read()
word = d.split()
for i in word:
    if  i[0].islower():
        f1.write(i)
        f1.write("\n")
f.close()
f1.close()
'''
##=========================================================================================================================================================================
##18.Write a program in Python to read file “data.txt” and copy only those lines to “story.txt” which are starting from alphabets “A” or “T”.
'''
f = open("data.txt", "r")
f1 = open("story.txt", "w")
d = f.readlines()
for i in d:
    if  i[0] == "A" or i[0] == "T":
        f1.write(i)
f.close()
f1.close()
'''
##=========================================================================================================================================================================
##19.Write a program in Python which display the longest word from file “star.txt”
'''
f = open("star.txt", "r")
d = f.read()
L = d.split()
longword = " "
for i in L:
    if  len(i) > len(longword):
      longword = i
print("longest word is ,",longword)
f.close()
'''
##=========================================================================================================================================================================
##20.Write a program in Python which display the longest line from file “star.txt”
'''
f = open("star.txt", "r")
d = f.readlines()
longline = " "
for i in d:
    if  len(i) > len(longline):
      longline = i
print("longest line is : ", longline)
f.close()
'''
##=========================================================================================================================================================================
##21.Write a program in Python to read the file “star.txt” and display the entire content after removing leading and trailing spaces.
'''
f = open("star.txt", "r")
d = f.readlines()
for i in d:
    print(i.strip())
f.close()
'''
##=========================================================================================================================================================================
##22.Write a program in python that read the content from file “sumit.txt” and display all numbers.
'''
f = open("sumit.txt", "r")
d = f.read()
for i in d:
  if i.isdigit():
    print(i)
f.close()
'''
##=========================================================================================================================================================================
##23.Write a program in Python that display the second and second last line from the file “life.txt”
'''
f = open("data.txt", "r")
d = f.readlines()
print("Second line is :",d[1])
print("Second last line is :",d[-2])
f.close()
'''
##=========================================================================================================================================================================
##24.Consider a binary file “data.dat” which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type. Do the following task in a file 
    ##1.Write a function addrec() to add a record in a file. 
    ##2.Write a function disp() to display all the records from the file. 
    ##3.Write a function specific_disp(room_no) which takes room number as argument and display its details. 
    ##4.Write a function mod(room_no) which takes room number as argument and modify it’s details.  
    ##5.Write a function del(room_no) which takes room number as argument and delete it’s record from file “data.dat” 
##=========================================================================================================================================================================
##25Write a menu driven program which shows all operations on Binary File 
##    1.Add Record 
##    2.Display All Record 
##    3.Display Specific Record 
##    4.Modify Record 
##    5.Delete Record 
##    6.Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type 
##=========================================================================================================================================================================
##26.Write a function disp75() in Python to display only those records of students from file “school.dat” who scored more than 75 percent marks. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##=========================================================================================================================================================================
##27.Write a function dispname() in Python which will display only names of all the students from file “school.dat”. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##=========================================================================================================================================================================
##28.Write a function disp12() in Python which will display records of class 12th students from file “school.dat”. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##=========================================================================================================================================================================
##29.Write a function search(name) in Python which will display record of a student from file “school.dat” whose name is passed as an argument. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##=========================================================================================================================================================================
##30.Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat” whose model number (integer type) is passed as an argument. Structure of “mobile.dat” is [Mobile id, Mobile brand, Model No., Price] 
