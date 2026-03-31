class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        path = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS
            or (r, c) in path or grid[r][c] == 0):
                return 0
            
            path.add((r, c))
            a = 1
            for dr, dc in dirs:
                a += dfs(r + dr, c + dc)
            
            return a
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        
        return res