##9. string = "Practice Problems to Drill List Comprehension in Your Head."
##Remove all of the vowels in a string (use string above)
##Find all of the words in a string that are less than 5 letters (use string above)
##Use a dictionary comprehension to count the length of each word in a sentence (use string above)
'''
a="Practice Problems to Drill List Comprehension in Your Head."
for i in a:
    if i not in ("a","e","i","o","u"):
        print(i,end="")
'''

##Output:Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd.

'''
a="Practice Problems to Drill List Comprehension in Your Head."
x=a.split()
for j in x:
    if len(j)<5:
        print(j,end=" ")
'''

##Output: to List in Your 

a="Practice Problems to Drill List Comprehension in Your Head."
s=a.split()
d={x:len(x) for x in s}
print(d)

##Output:
##{'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5}
