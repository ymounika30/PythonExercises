"""Counters->
A counter is a sub-class of the dictionary.
It is used to keep the count of the elements in an iterable in the form of an unordered dictionary
where the key represents the element in the iterable and value represents the count of that element in the iterable.
Note: It is equivalent to bag or multiset of other languages."""

##Syntax:
##
##class collections.Counter([iterable-or-mapping])

##from collections import Counter
##print(Counter([10,20,30,40,10,20,10,30,40]))


##op=Counter({10: 3, 20: 2, 30: 2, 40: 2})

"""OrderedDict->
An OrderedDict is also a sub-class of dictionary but unlike dictionary,
it remembers the order in which the keys were inserted. """

##Syntax:
##
##class collections.OrderDict()


##from collections import*
##    
##print("This is a Dict:\n") 
##d = {} 
##d['apple'] = 10
##d['ball'] = 20
##d['cat'] = 30
##d['dog'] = 40
##    
##for key, value in d.items(): 
##    print(key,":", value) 
##    
##print("\nThis is an Ordered Dict:\n") 
##od = OrderedDict() 
##od['cat'] = 30
##od['ball'] = 20
##od['dog'] = 40
##od['apple'] = 10
##od.pop('apple')
##od['app']=20
##    
##for key, value in od.items(): 
##    print(key,":", value)


"""DefaultDict->
A DefaultDict is also a sub-class to dictionary.
It is used to provide some default values for the key that does not exist and never raises a KeyError.

Syntax:

class collections.defaultdict(default_factory)

default_factory is a function that provides the default value for the dictionary created.
If this parameter is absent then the KeyError is raised."""
##from collections import*

##d=defaultdict(int)
##
##s=[10,20,30]
##for i in s:
##    d[i]+=1
##print(d)

##from collections import*
##d=defaultdict(list)
##for i in range(5):
##    d[i].append(i)
##
##print(d)


##from collections import*
##d=defaultdict(lambda:"0")
##d["apple"]=100
##d["banana"]=40
##
##print(d["apple"])
##print(d["orange"])


"""ChainMap
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.

Syntax:

class collections.ChainMap(dict1, dict2)"""

##from collections import*
##
##d1={"Raj":10,"Hari":20}
##d2={"apple":100,"banana":40}
##d3={"egg":5,"chicken":300}

##c=ChainMap(d1,d2,d3)
##print(c)
##print(c["Raj"])
##print(list(c.values()))
##print(list(c.keys()))

"""nwe_child()"""
##from collections import*
##
##d1={"Raj":10,"Hari":20}
##d2={"apple":100,"banana":40}
##d3={"egg":5,"chicken":300}
##
##c=ChainMap(d1,d2)
##print(c)
##c1=c.new_child(d3)
##print(c1)


"""NamedTuple->
A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack.
Syntax:

class collections.namedtuple(typename, field_names)
"""
##from collections import*
##
##Student=namedtuple('Student',['name','age','dob'])
##s=Student("Rakesh","23","08-07-1998")
##
##print(s.name)
##print(s[0])
##print(getattr(s,'age'))

"""UserList->

UserList is a list like container that acts as a wrapper around the list objects.
This is useful when someone wants to create their own list with some modified or additional functionality.

Syntax:

class collections.UserList([list])"""

##from collections import*

##l=[10,20,30]
##l1=UserList(l)
##print(l1.data)

##l2=UserList()
##print(l2.data)
"""UserDict->
This container is used when someone wants to create their own dictionary with some modified or new functionality.

Syntax:

class collections.UserDict([initialdata])"""



##from collections import UserDict
 
 
##d = {'a':1,
##    'b': 2,
##    'c': 3}
##d1=UserDict(d)
##print(d1.data)

##d3=UserDict()
##print(d3.data)


"""Deque->

Deque (Doubly Ended Queue) is the optimized list for quicker append and
pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.

Syntax:

class collections.deque(list)
This function takes the list as an argument."""
