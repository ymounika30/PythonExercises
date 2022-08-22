##3.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
class Paranthesis:
    def str_paranthesis(self,str_a):
        a,b=[],{"(":")","{":"}","[":"]"}
        for i in str_a:
            if i in b:
                a.append(i)
            elif len(a)==0 or b[a.pop()]!=i:
                return False
        return len(a)==0
print(Paranthesis().str_paranthesis("(){}[]"))
print(Paranthesis().str_paranthesis("()[{)}"))
print(Paranthesis().str_paranthesis("{}"))
      
    
