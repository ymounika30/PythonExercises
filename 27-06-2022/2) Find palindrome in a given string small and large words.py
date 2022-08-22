##2) Find palindrome in a given string small and large words?
##eg:- mom and dad speak malayalam with nitin
##mom
##dad
##malayalam
a=input().split()
b=[]
for i in a:
    if i==i[::-1]:
        b.append((len(i),i))
print(min(b))
print(max(b))
