class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #initialize pointers
        n = len(nums) # length of array
        res = [] # result is a list of lists
        nums.sort() # sorted array

        for i in range(n - 2): # goes up to n-3
            if i > 0 and nums[i] == nums[i -1] : 
                continue
            j = i + 1
            k = n - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    # skips duplicates for j
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # skips duplicates for k
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res
                






        
            
     

        
    