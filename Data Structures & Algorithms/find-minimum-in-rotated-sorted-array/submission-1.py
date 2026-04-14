class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 #initialize pointers
        res = nums[0] # initialize result for output

        while l <= r:
            mid = l + (r - l) // 2 # calculate middle element

            #if it's already sorted
            if nums[l] <= nums[r]:
                res = min(res,nums[l]) # result is the minimum element of rotated sorted array
                break
            res = min(res,nums[mid]) # update result 
            
            if nums[mid] >= nums[l]:
                # search for right half
                l = mid + 1 
            # search for left half 
            else: 
                r = mid - 1 
            



        
        return res