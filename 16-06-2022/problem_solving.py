##program:
##write a program to merge characters of two strings into single string by taking characters alternatively.
##Input:
##Take any two strings(note:The string contains alpha numeric characters also)
##ex:
##s1=""
##s2=""
##
##Output:
##The output should be a single string such a way that input strings characters are printed alternatively.
##
##Explanation:
##For example,if the given string1 is "gopi" and string2 is "venkat".
##
##The output should be "gvoepmikat"
##
##Example1:
##
##Sample Input:
##priya12
##45rohit
##Sample Output:
##p4r5iryoah1i2t
s1=input("enter frist string")
s2= input("enter second string")
output =''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i <len(s1):
        output+=s1[i]
        i+=1
    if j<len(s2):
        output+=s2[j]
        j+=1
print(output)
