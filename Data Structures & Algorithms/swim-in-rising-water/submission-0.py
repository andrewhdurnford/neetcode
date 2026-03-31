class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        heap = [[grid[0][0], [0, 0]]]
        path = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while len(path) < ROWS * COLS:
            cost, cur = heapq.heappop(heap)
            
            if tuple(cur) in path:
                continue
            path.add(tuple(cur))

            if cur == [COLS - 1, ROWS - 1]:
                return cost
            
            
            
            for dr, dc in dirs:
                x, y = cur[0] + dr, cur[1] + dc
                if (min(x, y) < 0 or x == ROWS or y == COLS
                    or (x, y) in path):
                    continue
                heapq.heappush(heap, [max(cost, grid[x][y]), [x, y]])
                
