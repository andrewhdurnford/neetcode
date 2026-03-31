class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(cur, o, c):
            if len(cur) == 2 * n:
                res.append(cur)
            
            if o < n:
                backtrack(cur + '(', o + 1, c)
            
            if c < o:
                backtrack(cur + ')', o, c + 1)

        backtrack('', 0, 0)
        return res