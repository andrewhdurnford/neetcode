class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        res = 0

        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev[1] <= cur[0]:
                prev = cur
                continue
            
            if prev[1] > cur[1]:
                prev = cur
            
            res += 1
        
        return res

