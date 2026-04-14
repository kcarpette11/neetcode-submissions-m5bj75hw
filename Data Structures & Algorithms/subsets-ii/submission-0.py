class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        n = len(nums)

        def backtrack(start):
            res.append(subset[:])

            for i in range(start,n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i]) #choose 
                backtrack(i+1) # explore other elements 

                subset.pop() #remove

        backtrack(0)
        return res