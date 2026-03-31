class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        end = intervals[0][1]
        res = 0

        for i, n in enumerate(intervals[1:]):
            if end <= n[0]:
                end = n[1]
            else:
                res += 1
                end = min(end, n[1])
        
        return res