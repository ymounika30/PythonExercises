##1) using functools write a program on partialmethod, lru_cache and total_ordering
from functools import*
'''
class Switch:
    def __init__(self):
        self._state = False
    def set_new_state(self, new_state: bool):
        self._state = new_state
    @property
    def state(self):
        return self._state
    turn_on = partialmethod(set_new_state, True)
    turn_off = partialmethod(set_new_state, False)
switch = Switch()
print("Turning on the switch: ", end="")
switch.turn_on()
print(switch.state)
print("Turning off the switch: ", end="")
switch.turn_off()
print(switch.state)
'''
##=================================================================================================================
'''
@lru_cache(maxsize = 100)
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')
      
print(count_vowels("Mounika is learning python language"))
'''

##===================================================================================================================
@total_ordering
class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa
  
    def __lt__(self, other):
        return self.cgpa<other.cgpa
s1=Student(8.6)
s2=Student(7.5)
print(s1==s2)
print(s1>s2)
print(s1<s2)
