class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #initialize two pointers
        i = 0 
        j = len(numbers) - 1
       
        # making sure the pointers do not cross
        while i < j:
            #Adjust the pointers based on the conditions
            curr_sum = numbers[i] + numbers[j] # sum of the 2 indices
            if curr_sum > target:
                 j -= 1
            elif curr_sum < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return []





            
        
        