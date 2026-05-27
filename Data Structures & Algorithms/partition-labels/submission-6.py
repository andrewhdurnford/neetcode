class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        
        res = []
        end = 0
        cur = 0

        for i, c in enumerate(s):
            cur += 1
            end = max(end, last[c])

            if i == end:
                res.append(cur)
                cur = 0
        
        return res

