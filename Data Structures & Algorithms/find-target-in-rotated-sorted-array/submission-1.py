class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) # length of input array
        l, r = 0, n -1 # initialize pointers

        while l <= r: # iterate through condition

            mid = (l + r) // 2 # calulate middle index/ element
            if nums[mid] == target: # if middle index is target
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    # target in sorted left half 
                   r = mid - 1
                else: 
                    l = mid + 1
            else: # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

             
            
               
               
        return -1 # if target is not found in array
        