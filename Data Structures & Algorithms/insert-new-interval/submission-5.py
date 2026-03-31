class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval
        for n, i in enumerate(intervals):
            if i[1] < start:
                res.append(i)
            elif end < i[0]:
                res.append([start, end])
                res.extend(intervals[n:])
                return res
            else:
                start = min(start, i[0])
                end = max(end, i[1])

        res.append([start, end])
        return res