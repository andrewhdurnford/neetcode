class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        pac, atl = set(), set()

        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS - 1, c))
        
        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS - 1))

        # PACIFIC
        q = deque(pac)

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0
                or nr == ROWS
                or nc == COLS
                or (nr, nc) in pac
                or heights[nr][nc] < heights[r][c]
                    ):
                    continue
                pac.add((nr, nc))
                q.append((nr, nc))

        # ATLANTIC
        q = deque(atl)

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0
                or nr == ROWS
                or nc == COLS
                or (nr, nc) in atl
                or heights[nr][nc] < heights[r][c]
                    ):
                    continue
                atl.add((nr, nc))
                q.append((nr, nc))
        
        res = []
        for r, c in pac:
            if (r, c) in atl:
                res.append([r, c])
        return res


