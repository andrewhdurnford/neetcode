class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [set() for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            adj[a - 1].add(b - 1)
            adj[b - 1].add(a - 1)
            degree[a - 1] += 1
            degree[b - 1] += 1
        
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            degree[node] -= 1
            for nei in adj[node]:
                adj[nei].remove(node)
                degree[nei] -= 1
                if degree[nei] == 1:
                    q.append(nei)
        
        print(degree)
        
        for a, b in reversed(edges):
            if degree[a - 1] == 2 and degree[b - 1] == 2:
                return [a, b]
