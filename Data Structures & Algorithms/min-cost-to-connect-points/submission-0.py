class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        def dist(xa, ya, xb, yb):
            return abs(xa - xb) + abs(ya - yb)

        for x, y in points:
            for xi, yi in points:
                adj[(x, y)].append([dist(x, y, xi, yi), (xi, yi)])
        
        path = set()
        cost = 0
        heap = [[0, tuple(points[0])]]

        while len(path) < len(points):
            c, cur = heapq.heappop(heap)
            if cur in path:
                continue
            cost += c
            path.add(cur)

            for nei in adj[cur]:
                if nei[1] not in path:
                    heapq.heappush(heap, nei)
        
        return cost

                


