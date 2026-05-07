class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, o, c):
            if o == c == n:
                res.append(cur)
                return
            
            if o < n:
                cur += '('
                backtrack(cur, o + 1, c)
                cur = cur[:-1]
            
            if c < o:
                cur += ')'
                backtrack(cur, o, c + 1)
                cur = cur[:-1]

        backtrack('',0,0)
        return res
            
