class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isP(s):
            return s == s[::-1]

        def dfs(cur, l):
            if l == len(s):
                res.append(cur.copy())
                return
            
            for r in range(l, len(s)):
                if isP(s[l : r + 1]):
                    cur.append(s[l : r + 1])
                    dfs(cur, r + 1)
                    cur.pop()
        
        dfs([], 0)
        return res