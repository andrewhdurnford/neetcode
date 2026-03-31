class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        ROWS, COLS = len(grid), len(grid[0])
        rotten = set()
        q = deque()

        def visit(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                grid[r][c] = 2
                rotten.add((r, c))
                q.append([r, c])
                return 1
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    rotten.add((r, c))

        t = 0
        while q:
           
            for i in range(len(q)):
                r, c = q.popleft()
                if (r, c) in rotten:
                    for dr, dc in dirs:
                        visit(r + dr, c + dc)
                        
            t += 1
  
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        if t > 0:
            return t - 1
        return t
