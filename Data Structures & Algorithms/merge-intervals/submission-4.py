class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(1, len(intervals)):
            cur, prev = intervals[i], intervals[i - 1]
            if cur[0] > prev[1]:
                res.append(prev)
            else:
                intervals[i] = [prev[0], max(prev[1], cur[1])]

        res.append(intervals[-1])

        return res