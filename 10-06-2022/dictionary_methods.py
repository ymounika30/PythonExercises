#clear()
dict1={
    "name": "mounika",
    "software": "python",
    }
dict1.clear()
print(dict1)
#-------------------------------
#copy()
dict2={
    "name": "mounika",
    "software": "python"
    }
dict3=dict2.copy()
print(dict3)
#-------------------------------
#fromkeys()
dict4={
    "name":"mounika",
    "software":"python"
    }
print(dict.fromkeys(dict4))
#-------------------------------------
#get
dict5={
    "name":"mounika",
    "software":"python"
    }
print(dict5.get("name"))
#----------------------------------------
#items
dict6={
    "name":"mounika",
    "software":"python"
    }
print(dict6.items())
#----------------------------------------
#keys
dict7={
    "name":"mounika",
    "software":"python"
    }
print(dict7.keys())
#------------------------------------
#values
dict8={
    "name":"mounika",
    "software":"python"
    }
print(dict8.values())
#-----------------------------------
#pop()
dict9={
    "name":"mounika",
    "software":"python"
    }
dict9.pop("name")
print(dict9)
#------------------------------------
#popitem()
dict10={
    "name":"mounika",
    "software":"python"
    }
dict10.popitem()
print(dict10)
#----------------------------------
#setdefault()
dict11={
    "name":"mounika",
    "software":"python"
    }
print(dict11.setdefault("software","java"))
#--------------------------------------------
#update()
dict12={
    "name":"mounika",
    "software":"python"
    }
dict12.update({"color":"red"})
print(dict12)
