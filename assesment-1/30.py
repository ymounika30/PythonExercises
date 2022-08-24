##30. Write a Python program to replace dictionary values with their average

dict1 = {
    "Scala": 2,
    "Javascript": 1,
    "Python": 8,
    "C++": 1,
    "Java": 4
    }
update_dict = {
    "Scala"  : 10,
    "Python" : 17
    }

print("Dictionary = ", end = " ")
print(dict1)
for i in dict1:
    if i in update_dict:
        dict1[i]  = update_dict[i]
print("Updated dictionary = ", end = " ")
print(dict1)


##Output:
##Dictionary =  {'Scala': 2, 'Javascript': 1, 'Python': 8, 'C++': 1, 'Java': 4}
##Updated dictionary =  {'Scala': 10, 'Javascript': 1, 'Python': 17, 'C++': 1, 'Java': 4}
