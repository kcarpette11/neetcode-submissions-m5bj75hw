class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        # sort the intervals in ascending order
        intervals.sort(key=lambda x: x[0] )

        #iterate through each list in the intervals 
        for interval in intervals:
            # if result is empty or no overlap with the last interval
            if not res or res[-1][1] < interval[0]:
                res.append(interval) # add interval to list
            
            else:
                #merge overlapping intervals
                res[-1][1]= max(res[-1][1],interval[1])


        return res
    
        
        