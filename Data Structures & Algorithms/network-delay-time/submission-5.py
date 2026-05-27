class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neis = [[] for _ in range(n + 1)]

        for source, target, t in times:
            neis[source].append((t, target))
        
        # djikstra's algorithm!!!
        # heap + visit set
        # init heap with k
        # at each node:
        # mark as visited
        # push all unvisited neighbors + time
        # heap item sohuld be (cumulative cost, node)

        heap = []
        heapq.heappush(heap, (0, k))
        visit = set()
        res = 0

        while heap:
            if len(visit) == n:
                return res

            t, cur = heapq.heappop(heap)
            if cur in visit:
                continue
            visit.add(cur)
            res = max(res, t)

            for nei in neis[cur]:
                if nei[1] not in visit:
                    item = [nei[0] + t, nei[1]]
                    heapq.heappush(heap, tuple(item))
        
        return res if len(visit) == n else -1
