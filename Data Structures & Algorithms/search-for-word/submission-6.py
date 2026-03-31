class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
            or board[r][c] != word[i] or (r, c) in path):
                return False
            
            if i == len(word) - 1:
                return True
            
            path.add((r, c))
            i += 1
            res = (dfs(r + 1, c, i) or
                    dfs(r - 1, c, i) or
                    dfs(r, c + 1, i) or
                    dfs(r, c - 1, i))
            path.remove((r, c))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        
        return False
        