class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        q = deque()
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                cur = grid[r][c]
                if cur == 1:
                    fresh += 1
                elif cur == 2:
                    q.append((r, c))
        
        while q:
            if fresh == 0:
                return time
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0
                        or nr == ROWS
                        or nc == COLS
                        or grid[nr][nc] != 1
                        ):
                        continue
                    rot = True
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        
        if fresh == 0:
            return time

        return -1 

        