class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the intervals
        intervals.sort(key=lambda x: x[0])

        res = 0

        prevEnd = intervals[0][1]



        for i in range(1, len(intervals)):
            start,end = intervals[i]

            if start >= prevEnd:
                #no overlap, update prevEnd
                prevEnd = end
            else:
                #overlap detected
                res += 1
                prevEnd = min(prevEnd,end)
        
            

        return res
        