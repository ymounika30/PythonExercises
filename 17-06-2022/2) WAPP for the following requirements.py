#2) WAPP for the following requirements
 #   input->a3z2b4
  #  output->aaabbbbzz(sorted string).'''


a='a3z2b4'
count=0
string1=''
string2=''
for i in a:
    if i.isdigit():
        string1=a[count-1]*int(i)
        string2=string2+string1
    count+=1   

mylist=sorted(string2)
string=''.join(mylist)
print(string)
