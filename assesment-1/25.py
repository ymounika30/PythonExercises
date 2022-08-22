##25. Write a Python program to find the occurrences of 10 most common words in a given text
def word_count(a):
    count = dict()
    word = a.split()
    for i in word:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
print( word_count("mounika is python learner, he is a ojas employee"))

#input: "mounika is python learner, he is a ojas employee"
#output: {'mounika': 1, 'is': 2, 'python': 1, 'learner,': 1, 'he': 1, 'a': 1, 'ojas': 1, 'employee': 1}
