class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums) # convert array into set
        set_count = len(my_set) # length of set
        num_count = len(nums)   
        if set_count != num_count:
            return True 
        else:
            return False   
    




        