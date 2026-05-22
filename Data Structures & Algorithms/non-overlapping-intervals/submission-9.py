class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        cur = intervals[0][1]

        for i in range(1, len(intervals)):
            if cur <= intervals[i][0]:
                cur = intervals[i][1]
            else:
                res += 1    
                cur = min(cur, intervals[i][1])
        
        return res
        