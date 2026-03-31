class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) >= 0 and nr < ROWS and nc < COLS 
                    and (nr, nc) not in visit and grid[nr][nc] != -1):
                        visit.add((nr, nc))
                        grid[nr][nc] = grid[r][c] + 1
                        q.append([nr, nc])
        
        

