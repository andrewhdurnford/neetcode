class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(len(edges) + 1)]
        
        def dfs(node, par):
            if node in visited:
                return True
            
            visited.add(node)

            for nei in adj[node]:
                if not nei == par and dfs(nei, node):
                    return True

            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
        
            if dfs(u, -1):
                return [u, v]

        return []
        