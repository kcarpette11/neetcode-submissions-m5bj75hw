class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles) # length of array
        left = 1 #Initialize pointers
        right = max(piles) # right pointer is the max amount of array

        k = right 
      

        while left <= right:
            # calculating k, which is the middle element
            k = left + (right - left) // 2
            total_hours = 0 # initialize amount of hours 

            for pile in piles:
                total_hours += (pile + k -1) // k # ceiling division

            if total_hours == h:
               right = k - 1 
            elif total_hours < h:
                right = k - 1
            else:
                left = k + 1
              
            
           
        return left 





        