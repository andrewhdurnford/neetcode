class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n
        path = set()

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node, p):
            nonlocal count
            if node in path:
                return
            path.add(node)

            for n in adj[node]:
                dfs(n, node)

            if not p == -1:
                count -= 1
            
        
        for i in range(n):
            dfs(i, -1)

        return count
