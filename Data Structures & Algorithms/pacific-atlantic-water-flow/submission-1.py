class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        pac = set()
        atl = set()

        def bfs(r, c, visit, h):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or heights[r][c] < h):
                return
            
            visit.add((r, c))

            for dr, dc in dirs:
                bfs(r + dr, c + dc, visit, heights[r][c])
        
        for r in range(ROWS):
            bfs(r, 0, pac, heights[r][0])
            bfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        for c in range(COLS):
            bfs(0, c, pac, heights[0][c])
            bfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        res = []

        for p in pac:
            if p in atl:
                res.append([p[0], p[1]])
        
        return res