##20. Write a python program on filtering consonants 
## 
##Note the following points: 
##1.	The method should scan the given input, remove all the consonants and return the resulting string. 
##2.	The output should contain only vowels and all other characters, including special characters should be filtered out. 
##3.	If input is null, return null. 
##4.	Example input: “Telephone”, Output: “eeoe” 
a=input()
for i in a:
    if i in("a,e,i,o,u"):
        print(i, end="")


##Input: “Telephone”,
##Output: “eeoe”
