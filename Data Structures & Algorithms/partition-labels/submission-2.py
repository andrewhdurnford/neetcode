class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        
        chars = set()
        cur = 0
        res = []

        for i,c in enumerate(s):
            cur += 1  
            chars.add(c)
            
            if i == last[c]:
                chars.remove(c)
            
            if len(chars) == 0:
                res.append(cur)
                cur = 0
        
        return res

            

