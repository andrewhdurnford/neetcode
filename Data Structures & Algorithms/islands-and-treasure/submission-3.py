class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, i):   
            grid[r][c] = i

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or
                    nr == ROWS or
                    nc == COLS or
                    i >= grid[nr][nc] or
                    grid[nr][nc] <= 0
                    ):
                    continue
                grid[nr][nc] = i
                dfs(nr, nc, i + 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
        
        print(grid)