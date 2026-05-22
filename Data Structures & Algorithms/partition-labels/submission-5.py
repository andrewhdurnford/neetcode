class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        end = 0
        cur = 0
        res = []

        for i, c in enumerate(s):
            end = max(end, last[c])
            cur += 1

            if i == end:
                res.append(cur)
                cur = 0

        return res
            
