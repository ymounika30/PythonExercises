##Max Contiguous Subarray: Given a list of integers, write a program to identify contiguous sub-list that has the largest sum and print the sub-list. Any non-empty slice of the list with step
##size 1 can be considered as contiguous sub-list.
##
##Input:
##The input will contain space-separated integers,
##denoting the elements of the list.
##
##Output
##The output should be space-separated integers.
##
##Explanation
##For example, if the given list is [2, -4, 5, -1, 2,
##-3], then all the possible contiguous sub-lists
##will be,
##Explanation
##For example, if the given list is [2, -4, 5, -1, 2,
##-3], then all the possible contiguous sub-lists
##will be,
##[2]
##[2,-4]
##[2,-4, 5]
##[2,-4, 5, -1]
##[2,-4, 5, -1, 2]
##[2,-4, 5, -1, 2, -3]
##[-4]
##[-4, 5]
##[-4, 5, -1]
##[-4, 5, -1, 2]
##[-4, 5, -1, 2, -3]
##[5]
##[5, -1]
##[5, -1, 2]
##[5, -1, 2, -3]
##[-1]
##[-1, 2]
##[-1, 2, -3]
##[2]
##[2, 3]
##[-3]
##
##Sample Input 1
##2 -4 5 -1 2 -3
##Sample Output 1
##5 -1 2
##Sample Input 2
##-2 -3 4 -1 -2 1 5 -3
##Sample Output 2
##4 -1 -2 1 5
l1 =[-2, -3, 4, -1, -2, 1, 5, -3]
lists=[]
aa=[]
k=[]
for i in range(len(l1)+1):
    for j in range(i):
        lists.append(l1[j:i])
for i in lists:
    aa.append(i)
    add=0
    for j in i:
        add+=j
    k.append(add)
index_a=k.index(max(k))
print(aa[index_a])


