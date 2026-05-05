class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(r, c, path, idx):
            if board[r][c] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            path.add((r, c))

            for dr, dc in dirs:
                if (min(r + dr, c + dc) < 0 
                or r + dr == ROWS or c + dc == COLS 
                or (r + dr, c + dc) in path):
                    continue
                if backtrack(r + dr, c + dc, path, idx + 1):
                    return True
            
            path.remove((r, c))
            
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, set(), 0):
                    return True

        return False
            
