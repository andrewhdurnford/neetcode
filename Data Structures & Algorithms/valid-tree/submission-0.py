class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        path = set()
        al = {i: [] for i in range(n)}
        for n1, n2 in edges:
            al[n1].append(n2)
            al[n2].append(n1)
        
        def dfs(n, p):
            if n in path:
                return False
            
            path.add(n)

            for node in al[n]:
                if node == p:
                    continue
                if not dfs(node, n):
                    return False
            return True
        
        return dfs(0, -1) and len(path) == n
