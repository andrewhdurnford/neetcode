class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isP(s):
            return s == s[::-1]
        
        def backtrack(cur, l, r):
            if r > len(s):
                if l == r - 1:
                    res.append(cur.copy())
                return

            backtrack(cur, l, r + 1)

            if isP(s[l:r]):
                cur.append(s[l:r])
                backtrack(cur, r, r + 1)
                cur.pop()
            
        backtrack([],0,1)
        return res
