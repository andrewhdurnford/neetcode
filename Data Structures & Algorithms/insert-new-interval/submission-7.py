class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        insert = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]
            if insert[1] < start:
                res.append(insert)
                res.extend(intervals[i:])
                return res

            if end < insert[0]:
                res.append(intervals[i])
                continue
            
            insert = [min(start, insert[0]), max(end, insert[1])]
        
        res.append(insert)
        return res