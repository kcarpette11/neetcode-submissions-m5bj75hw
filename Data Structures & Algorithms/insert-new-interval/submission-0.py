class Solution:
     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        l, r = 0, len(intervals) - 1

        if not intervals:
            return [newInterval]

        while l <= r:
            if intervals[l][1] < newInterval[0]:
                res.append(intervals[l])
            elif intervals[l][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[l:]
            else:
                newInterval = [
                    min(newInterval[0], intervals[l][0]),
                    max(newInterval[1], intervals[l][1])
                ]

            l += 1

        res.append(newInterval)
        return res