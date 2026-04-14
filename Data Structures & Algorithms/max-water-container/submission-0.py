class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) # length of array
        #initialize pointers

        i = 0
        j = n - 1
        res = 0 # initialize result

        while i < j:
            water_amount = (j - i) * min(heights[i], heights[j]) # calculate formula


          

            res = max(res, water_amount) # finding  max water among all pairs 
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1




        
        return res



        
        