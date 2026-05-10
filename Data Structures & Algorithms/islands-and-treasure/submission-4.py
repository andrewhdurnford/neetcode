class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    min(nr, nc) < 0
                    or nr == ROWS
                    or nc == COLS
                    or (nr, nc) in visit
                    or grid[nr][nc] <= 0
                    ):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                visit.add((nr, nc))
                q.append((nr, nc))
        