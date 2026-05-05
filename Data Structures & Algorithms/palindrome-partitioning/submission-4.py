class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isP(s):
            return s == s[::-1]
        
        def backtrack(l, cur):
            if l == len(s):
                res.append(cur.copy())
                return
            
            for r in range(l + 1, len(s) + 1):
                sub = s[l:r]
                if isP(sub):
                    cur.append(sub)
                    backtrack(r, cur)
                    cur.pop()

        backtrack(0, [])
        return res
