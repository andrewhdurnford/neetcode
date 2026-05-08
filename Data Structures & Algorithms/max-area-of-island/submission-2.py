class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            cur = 1
            grid[r][c] = 0

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0
                    or nr == ROWS
                    or nc == COLS
                    or grid[nr][nc] == 0):
                    continue
                cur += dfs(nr, nc)

            return cur
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    cur = dfs(r, c)
                    res = max(res, cur)
        
        return res
            