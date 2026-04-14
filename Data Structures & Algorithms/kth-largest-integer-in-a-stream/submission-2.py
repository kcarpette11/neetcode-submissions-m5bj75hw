import heapq # using heap
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initialize the variables
        self.k = k 
        self.min_heap = [] # for holding the largest kth elements 
        for num in nums:
            heapq.heappush(self.min_heap,num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

        

    def add(self, val: int) -> int:
        self.val = val
        heapq.heappush(self.min_heap,self.val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
      
        
        
       
        
