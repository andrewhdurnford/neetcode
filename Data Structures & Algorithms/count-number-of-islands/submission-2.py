class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            nonlocal res
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            for dr, dc in dirs:
                if (min(r + dr, c + dc) < 0
                    or r + dr == ROWS
                    or c + dc == COLS):
                    continue
                
                dfs(r + dr, c + dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        
        return res
            
