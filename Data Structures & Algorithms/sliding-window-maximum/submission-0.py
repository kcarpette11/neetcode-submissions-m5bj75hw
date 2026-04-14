import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
     # using heap
     heap = []
     res = []
     n = len(nums)

    

     for i in range(n):
        # Add negatives values to heap 
        heapq.heappush(heap,(-nums[i],i))

        #remove elements outside the window
        while heap[0][1] <= i - k:
            heapq.heappop(heap) 
        if i >= k - 1: # add positive values to result array
            res.append(-heap[0][0])
    



     return res
    
     
        