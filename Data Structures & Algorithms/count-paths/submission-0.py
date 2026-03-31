class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for c in range(COLS):
            grid[0][c] = 1
        
        for r in range(ROWS):
            grid[r][0] = 1
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[-1][-1]