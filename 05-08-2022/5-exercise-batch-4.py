'''1) write a program on magical method add , pos and neg?'''
##class Magic:
##    def __init__(self,a):
##        self.a=a
##    def __add__(self,other):
##        return self.a+other.a
##    def __pos__(self):
##        return self.a
##    def __neg__(self):
##        return self.a[:1]
##obj1=Magic("10")
##obj2=Magic("2")
##print(obj1+obj2)
##print(+obj1)
##print(-obj1)
        
##===================================================================================================================================
'''2) write a program convert day number to date in particular year?'''
##from datetime import datetime
##day_num = "339"
##print("The day number : " + str(day_num))
##day_num.rjust(3 + len(day_num), '0')
##year = "2020"
##res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%m-%d-%Y")
##print("Resolved date : " + str(res))
##===================================================================================================================================
'''3) write a dictionary to a file in python?'''
##import json
##details = {'Name': "Bob",
##          'Age' :28}
##with open('convert.txt', 'w') as convert_file:
##     convert_file.write(json.dumps(details))
##===================================================================================================================================
'''4) find the most repeated word in a text file?'''
##file = open("convert.txt","r")
##frequent_word = ""
##frequency = 0 
##words = []
##for line in file:
##    line_word = line.lower().replace(',','').replace('.','').split(" ")
##    for w in line_word: 
##        words.append(w) 
##for i in range(0, len(words)):
##    count = 1
##    for j in range(i+1, len(words)): 
##        if(words[i] == words[j]): 
##            count = count + 1
##    if(count > frequency):
##        frequency = count
##        frequent_word = words[i] 
##print("Most repeated word: " + frequent_word)
##print("Frequency: " + str(frequency))
##file.close()
##===================================================================================================================================
'''5) write a program on sprial number?

eg:-1 2 3
    8 9 4
    7 6 5'''
x=1
a=[1,2,3,8,9,4,7,6,5]
b=[1,2,3,4,5,6,7,8,9]
for i in a:
    b[i-1]=x
    x+=1
y=0
for i in a:
    print(i, end=" ")
    y+=1
    if y%3==0:
        print()
