class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for f, t in tickets:
            heapq.heappush(adj[f], t)
        
        path = ['JFK']
        cycle = []

        while len(path) > 0:
            cur = path[-1]
            if len(adj[cur]) > 0:
                nxt = heapq.heappop(adj[cur])
                path.append(nxt)

            else:
                cycle.append(path.pop())
        
        cycle.reverse()
        return cycle

        
