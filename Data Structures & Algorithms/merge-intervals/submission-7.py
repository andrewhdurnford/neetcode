class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort() # start(n) <= start(n + 1) <= end(n + 1)
        cur = intervals[0]

        for i in range(1, len(intervals)):
            nxt = intervals[i]
            if cur[1] < nxt[0]: # end of insert < start of next
                res.append(cur)
                cur = nxt
            else:
                cur = [min(cur[0], nxt[0]), max(cur[1], nxt[1])]
        
        res.append(cur)
        return res
            
            

            
