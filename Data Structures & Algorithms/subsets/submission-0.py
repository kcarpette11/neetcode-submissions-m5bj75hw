class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]: 
        res = []
        subset = [] #initialize result array and subset

        def backtrack(start):
            #Base Case: check if solution meets the criteria
            # check for possible subsets of nums
            
            res.append(subset[:]) # make copy of array and add to result

            for i in range(start,len(nums)):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()





        backtrack(0)
        return res

        