class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # length of array 
        res = [1] * n  # adding 1 into list
        for i in range(n):
            for j in range(n):
                if i != j:
                    res[i] *= nums[j]
        return res
            


        

        