class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        end = intervals[0][1]

        for s, e in intervals[1:]:
            if end <= s:
                end = max(end, e)
                continue
            
            # elif end > s:
            res += 1
            end = min(end, e)

        return res

