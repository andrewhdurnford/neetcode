class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            valid = min(r, c) >= 0 and r < ROWS  and c < COLS
            if not valid or word[i] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            i += 1
            res = (dfs(r + 1, c, i) or
                    dfs(r - 1, c, i) or
                    dfs(r, c + 1, i) or
                    dfs(r, c - 1, i))
            i -= 1
            path.remove((r, c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
