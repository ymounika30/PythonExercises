##4.#Write a Python program to find the list with maximum and minimum length using lambda.
def max_length_list(a):
    max_length = max(len(x) for x in a )   
    max_list = max(a, key = lambda i: len(i))    
    return(max_length, max_list)
def min_length_list(a):
    min_length = min(len(x) for x in a )   
    min_list = min(a, key = lambda i: len(i))    
    return(min_length, min_list)
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print(max_length_list(list1))
print(min_length_list(list1))
