##4.Write a Python class to get all possible unique subsets from a set of distinct integers.
##Input : [4, 5, 6]
##Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
class Uniquesubsets:
    def unique_subset(self,set1):
        return self.subsets([],sorted(set1))
    def subsets(self,current,set1):
        if set1:
            return self.subsets(current,set1[1:])+self.subsets(current+[set1[0]],set1[1:])
        return [current]
print(Uniquesubsets().unique_subset([4,5,6]))
        
