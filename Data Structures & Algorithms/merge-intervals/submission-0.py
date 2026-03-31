class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []

        for i in range(len(intervals)):
            if i == len(intervals) - 1:
                res.append(intervals[i])
            elif intervals[i][1] < intervals[i + 1][0]:
                res.append(intervals[i])
            elif intervals[i][1] >= intervals[i + 1][0]:
                interval = [
                    min(intervals[i][0], intervals[i + 1][0]),
                    max(intervals[i][1], intervals[i + 1][1])
                ]
                intervals[i + 1] = interval
                i += 1

        return res
