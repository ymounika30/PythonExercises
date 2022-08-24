#add
set1={1,2,"hello",5.6}
set1.add("mounika")
print(set1)
#------------------------------------
#clear
set2={1,2,"hello",5.6}
set2.clear()
print(set2)
#-----------------------------------
#copy
set3={1,2,"hello",5.6}
set4={1,2,"mounika",5.6}
set4=set4.copy()
print(set4)
#----------------------------------
#difference
set5={1,2,"hello",5.6}
set6={1,2,3,4,5}
print(set5-set6)
#---------------------------------
#difference update
set6={1,2,"hello",5.6}
set7={1,2,3,4,5,6}
set6.difference_update(set7)
print(set6)
#------------------------------
#discard
set8={1,2,"hello",5.6}
set8.discard("hello")
print(set8)
#------------------------------
#intersection
set9={1,2,"hello",5.6}
set10={1,2,3,4,5,6}
print(set9.intersection(set10))
#--------------------------------
#intersection update
set11={1,2,"hello",5.6}
set12={1,2,3,4,5,6}
set11.intersection_update(set12)
print(set11)
#--------------------------------------
#isdisjoint
set13={1,2,"hello",5.6}
set14={3,4,5,6}
print(set13.isdisjoint(set14))
#-------------------------------------
##issubset()
set15={"a", "b", "c"}
set16={"f", "e", "d", "c", "b", "a"}
print(set15.issubset(set16))
#--------------------------------------
#issuperset()
set17={"f", "e", "d", "c", "b", "a"}
set18={"a", "b", "c"}
print(set17.issuperset(set18))
#--------------------------------------
#pop
set19={1,2,"hello",5.6}
set19.pop()
print(set19)
#--------------------------------------
#remove()
set20={1,2,"hello",5.6}
set20.remove(5.6)
print(set20)
#--------------------------------------
#symmetric_difference
set21={1,2,"hello",5.6}
set22={1,2,3,4,5,6}
print(set21.symmetric_difference(set22))
#------------------------------------------
#symmetric difference update
set23={"apple", "banana", "cherry"}
set24={"google", "microsoft", "apple"}
set23.symmetric_difference_update(set24) 
print(set23)
#---------------------------------------------
#union
set25={"apple", "banana", "cherry"}
set26={"google", "microsoft", "apple"}
print(set25.union(set26))
#--------------------------------------------------
set27={"apple", "banana", "cherry"}
set28={"google", "microsoft", "apple"}
set27.update(set28)
print(set27)

