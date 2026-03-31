class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p, a = set(), set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visit, pH):
            if ((r, c) in visit or min(r, c) < 0
                or r == ROWS or c == COLS or heights[r][c] < pH):
                return
            
            visit.add((r, c))
            
            for dr, dc in dirs:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, p, heights[0][c])
            dfs(ROWS - 1, c, a, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, p, heights[r][0])
            dfs(r, COLS - 1, a, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in p and (r, c) in a:
                    res.append([r, c])
        
        return res

