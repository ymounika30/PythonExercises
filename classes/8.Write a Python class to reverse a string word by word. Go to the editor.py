##8.Write a Python class to reverse a string word by word. Go to the editor
##Input string : 'hello .py'
##Expected Output : '.py hello'
class Reverse:
    def reverse_str(self,a):
        return ' '.join(reversed(a.split()))
print(Reverse().reverse_str("hello .py"))
