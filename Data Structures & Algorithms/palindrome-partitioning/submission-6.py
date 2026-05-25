class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isP(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]: return False
                l, r = l + 1, r - 1
            return True

        def backtrack(cur, i):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if isP(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    backtrack(cur, j + 1)
                    cur.pop()
        
        backtrack([], 0)
        return res