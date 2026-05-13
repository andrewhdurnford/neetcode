class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        s, e = newInterval
        
        for i, interval in enumerate(intervals):
            si, ei = interval

            if ei < s:
                res.append([si, ei])
                continue

            if e < si:
                res.append([s, e])
                res.extend(intervals[i:])
                return res
    
            else:
                s, e = min(s, si), max(e, ei)

        res.append([s, e])
        return res
