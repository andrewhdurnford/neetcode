class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        cols = set() # c
        posDiag = set() # r + c
        negDiag = set() # r - c

        def backtrack(r):
            if r == n:
                sol = []
                for i in range(n):
                    sol.append(''.join(board[i]))
                res.append(sol)
                return
            
            for c in range(n):
                if (
                    c in cols or
                    (r + c) in posDiag or
                    (r - c) in negDiag):
                    continue
                
                cols.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))
                board[r][c] = 'Q'
                backtrack(r + 1)
                cols.remove(c)
                board[r][c] = '.'
                posDiag.remove((r + c))
                negDiag.remove((r - c))
        
        backtrack(0)

        return res
        
                


