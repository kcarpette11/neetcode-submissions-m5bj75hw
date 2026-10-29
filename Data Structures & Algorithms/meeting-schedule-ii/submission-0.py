"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        n = len(intervals)

        rooms = [] # track any meetings 
        res = 0 

        for i in range(n):
            while rooms and rooms[0] <= intervals[i].start:
                heapq.heappop(rooms) # remove any meetings

            heapq.heappush(rooms,intervals[i].end)
            res = max(res,len(rooms))
    
        return res
    