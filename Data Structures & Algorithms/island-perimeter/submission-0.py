class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    
                    for dr, dc in dirs:
                        
                        nr, nc = r + dr, c + dc
                        if min (nr, nc) >= 0 and nr < ROWS and nc < COLS:
                            if not grid[nr][nc]:
                                res += 1
                        else:
                            res += 1
        
        return res
