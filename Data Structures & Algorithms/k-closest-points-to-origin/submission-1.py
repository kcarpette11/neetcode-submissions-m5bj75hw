import heapq  #using heap
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        min_heap = [] #initialize heap
        for x, y in points:
            # calculate distance formula 
            distance = math.sqrt((x *x)+ (y * y))
            heapq.heappush(min_heap,[distance,x,y])
        while k > 0:
            distance, x, y = heapq.heappop(min_heap)
            res.append([x,y])
            k -= 1

        return res 


        