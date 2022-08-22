'''1) wap to print all elements in nested lists as shown in below
l = [1,2,[3,4,[5,6],7],8]
output = 1 2 3 4 5 6 7 8'''
##lst = [1,2,[3,4,[5,6],7],8]
##def recur(lst):
##    for i in lst:
##        if type(i)==list:
##            recur(i)
##        else:
##            print(i)
##recur(lst)

##========================================================================================

'''2) Python code to demonstrate working of
 Convert Nested dictionary to Mapped Tuple
Using list comprehension + generator expression

input:
test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},
'best' : {'x' : 8, 'y' : 3}}

output:
The grouped dictionary : [(‘x’, (5, 1, 8)), (‘y’, (6, 4, 3))]'''

##test = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},
##'best' : {'x' : 8, 'y' : 3}}
##x = ['x']
##y = ['y']
##
##for k,v in test.items():
##   for key,value in v.items():
##       if key == 'x':
##           x.append(v[key])
##       if key == 'y':
##           y.append(v[key])
##lst = [tuple(x),tuple(y)]
##print(lst)

##===============================================================================================

'''3) Convert list of dictionaries to dictionary of lists Using dictionary comprehension.

input:
[{'name': 'sravan', 'subjects': ['java', 'python']},
{'name': 'bobby', 'subjects': ['c/cpp', 'java']},
{'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
{'name': 'rohith', 'subjects': ['php', 'os']},
{'name': 'gnanesh', 'subjects': ['html', 'sql']}]

output:
{'bobby': {'name': 'bobby', 'subjects': ['c/cpp', 'java']},
 'gnanesh': {'name': 'gnanesh', 'subjects': ['html', 'sql']},
 'ojsawi': {'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
 'rohith': {'name': 'rohith', 'subjects': ['php', 'os']},
 'sravan': {'name': 'sravan', 'subjects': ['java', 'python']}}'''
lst = [{'name': 'sravan', 'subjects': ['java', 'python']},
{'name': 'bobby', 'subjects': ['c/cpp', 'java']},
{'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
{'name': 'rohith', 'subjects': ['php', 'os']},
{'name': 'gnanesh', 'subjects': ['html', 'sql']}]

##dic = {i['name']:i for i in lst}
##print(dic)

##===================================================================================================

'''4) Python  code to demonstrate
# Least Frequent Character in String
The original string is :aaabbbcdddrrreeee
The minimum of all characters in GeeksforGeeks is : c'''
##string = 'aaaaabbbcddddrrreeee'
##small = string.count(string[0])
##for i in string:
##    if string.count(i)<small:
##        small = string.count(i)
##        c = i
##print(c)

##===============================================================================================

'5) wap to modify the existing method in a class after object creation (monkey pacthing)'
##class Parent:
##    def info(self):
##        print('this is before monkey patching')
##
##def details():
##    print('this is after monkey patching')
##
##obj = Parent()
##obj.info()
##obj.info = details
##obj.info()
