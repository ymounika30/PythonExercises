##9.Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
class GetString:
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input()
    def print_string(self):
        print(self.str1.upper())
str1=GetString()
str1.get_string()
str1.print_string()
