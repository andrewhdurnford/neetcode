class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        visit = set()
        q = deque()
        count = 0

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        for a in range(n):
            if a not in visit:
                q.append(a)
                visit.add(a)
                count += 1

                while q:
                    node = q.popleft()
                    for nei in adj[node]:
                        # if node in adj[nei]:
                        if nei not in visit:
                            adj[nei].remove(node)
                            visit.add(nei)
                            q.append(nei)
        
        return count
