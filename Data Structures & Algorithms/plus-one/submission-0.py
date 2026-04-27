class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []  # initialize result
        n = len(digits)
       
        for i in range(n - 1, -1,-1):
            if digits[i] < 9: # if less than 9, add digits[i] by 1
                digits[i] += 1
                return digits #stop if done 
            else: # if not, set it to 0
                digits[i] = 0
        res = [1] + digits # update result 

            
        

        return res # return result
