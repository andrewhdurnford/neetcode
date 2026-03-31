class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        fresh = 0
        t = 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        fresh -= 1
            t += 1

        return t if fresh == 0 else -1
