#append
list_1=[1,2,3,4]
list_1.append(5)
print(list_1)
#--------------------------------------------------
#clear
list2=[1,2,3,4]
list2.clear()
print(list2)
#---------------------------------------------------
#copy
list3=[1,2,3,4]
list4=list3.copy()
print(list4)
#---------------------------------------------------
#count
list5=[1,2,3,3,4]
list6=list5.count(3)
print(list5)
#---------------------------------------------------
#extend
list6=[1,2,3,4,5]
list7=[4,5,6,7,8]
list6.extend(list7)
print(list6)
#---------------------------------------------------
#index
list8=[1,2,3,4,5,6,7,8,9,10]
list9=list8.index(4)
print(list9)
#--------------------------------------------------
#insert
list10=[1,2,3,4,5,6]
list10.insert(2,5)
print(list10)
#--------------------------------------------------
#pop
list11=[1,2,3,4,5,6]
list11.pop()
print(list11)
#--------------------------------------------------
#remove
list12=[1,2,3,4,5,6]
list12.remove(3)
print(list12)
list13=[1,2,3,3,4]
list13.remove(3)
print(list13)
#--------------------------------------------------------
#reverse
list14=[1,2,3,4]
list14.reverse()
print(list14)
#--------------------------------------------------------
#sort
list15=[1,5,3,7,9,2,0]
list15.sort()
print(list15)
#-------------------------------------------------------
#sort_reverse
list16=[1,5,3,7,9,2,0]
list16.sort(reverse=True)
print(list16)
#------------------------------------------------------------
#minimum
list17=input()
list18=[]
for i in list17.split():
    list18+=[int(i)]
print(max(list18))
print(min(list18))
print(sum(list18))

