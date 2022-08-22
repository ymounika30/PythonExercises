##5.a.  Assign a different name to function and call it through the new name
'''
def name(a):
    print(a)
name("Mounika")
new_name=name
new_name("Laxmi")
'''

##Output:
##Mounika
##Laxmi


##b. 15.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
def sal(emp,salary=9000):
    print("employee",emp)
    print("Salary", salary)
sal("Mounika",3000)
sal("Laxmi")

##Output:
##employee Mounika
##Salary 3000
##employee Laxmi
##Salary 9000
