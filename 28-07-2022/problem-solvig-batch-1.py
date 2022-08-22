##1.You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code.
##The sentence you want to encode is "the lazy dog jumped over the quick brown fox."
##and the
##output should be "vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz."
##
##I/P-"The lazy dog jumped over the quick brown fox."
##
##O/P-"vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz."
list1='abcdefghijklmnopqrstuvwxyzab'
dict1={}
t=2
for i in list1[:-2]:
    dict1[i]=list1[t]
    t=t+1

a='the lazy dog jumped over the quick brown fox'
b=''
for i in a:
    if i!=' ':
        b=b+dict1[i]
    else:
        b=b+i
print(b)
    
        
    
