from collections import Counter
import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        if k <= 0 or not nums:
            return []
        freq_map = Counter(nums)
        min_heap = []
        for num,freq in freq_map.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return[num for freq, num in min_heap]
      
       

        
     
                

        