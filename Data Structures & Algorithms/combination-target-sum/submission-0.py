class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() # sort array from least to greatest 
        path = [] # for finding any paths

        def backtrack(start,target):
            if target < 0:
                return
            if target == 0:
                res.append(path[:]) # copy current path
                return 
            n = len(nums)
            for i in range(start,n):
                path.append(nums[i])
                backtrack(i,target-nums[i])
                path.pop() 
        

        backtrack(0,target)




        return res
    
        
        