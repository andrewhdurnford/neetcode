class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        res = []

        for i, interval in enumerate(intervals):
            if i == len(intervals) - 1:
                res.append(interval)
            elif interval[1] < intervals[i + 1][0]:
                res.append(interval)
            else:
                interval = [
                    min(interval[0], intervals[i + 1][0]),
                    max(interval[1], intervals[i + 1][1])
                ]
                intervals[i + 1] = interval
        
        return res