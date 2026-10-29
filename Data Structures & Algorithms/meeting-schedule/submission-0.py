"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        n = len(intervals)
        for i in range(1,n):
            i1, i2 = intervals[ i - 1], intervals[i]

            if i1.end > i2.start:
                return False
        
        return True

             



