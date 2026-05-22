class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)
        chars = set()
        cur = 0
        res = []

        for c in s:
            cur += 1
            chars.add(c)
            cnt[c] -= 1
            if cnt[c] == 0:
                chars.remove(c)
                if len(chars) == 0:
                    res.append(cur)
                    cur = 0
        
        return res
