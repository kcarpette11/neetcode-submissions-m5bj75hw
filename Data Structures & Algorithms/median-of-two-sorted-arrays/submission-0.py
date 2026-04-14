class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Do Brute Force
        nums = nums1 + nums2 # merge both arrays
        nums.sort() # array is sorted

        nums_count = len(nums) # length of array 

        # if length of array is even
        if nums_count % 2 == 0:
            return (nums[nums_count // 2 - 1] + nums[nums_count // 2]) / 2.0 
        #if it's odd
        else:
            return nums[nums_count // 2]



    

      