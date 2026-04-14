class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # convert list into set
        longest = 0
        for num in nums: # iterate through array
            if (num - 1) not in num_set:
                current_num = num
                length = 1 
                while (num + length) in num_set:
                
                    length += 1
                longest = max(length,longest)
        return longest


        