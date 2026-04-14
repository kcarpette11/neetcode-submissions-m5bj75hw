class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using hash set
            my_set = set(nums) # convert array into set
            set_count = len(my_set) # length of set
            num_count = len(nums)   
            for i in range(num_count):
                if set_count != num_count:
                    for num in nums:
                        if nums.count(num) > 1:
                            return num
                  
            
                else:
                    return -1 
    

        
        