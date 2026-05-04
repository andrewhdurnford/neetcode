class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, o, c):
            if o == c == n:
                res.append(''.join(cur.copy()))
                return
            
            if o < n:
                cur.append('(')
                backtrack(cur, o + 1, c)
                cur.pop()
            
            if c < o:
                cur.append(')')
                backtrack(cur, o, c + 1)
                cur.pop()

        backtrack([],0,0)
        return res
            
