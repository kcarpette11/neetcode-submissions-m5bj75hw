class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        n = len(nums) # n is the length of array
        left = 0  # initialize the indices
        right = n - 1
        mid = 0 # initialize middle index 

        while left <= right:
            mid = left + ( right - left) // 2 # for finding middle index 
            if nums[mid] == target:
                return mid # returns middle index
                
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1 # return target value if it is not found 

        