class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            grid[r][c] = '0'
            q = deque()
            q.append((r, c))

            while q:
                r, c = q.popleft()

                for dr, dc in dirs:
                    if (min(r + dr, c + dc) < 0
                        or r + dr == ROWS
                        or c + dc == COLS
                        or grid[r + dr][c + dc] == '0'):
                        continue
                    q.append((r + dr, c + dc))
                    grid[r + dr][c + dc] = '0'
                
                
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r, c)
        
        return res
            
