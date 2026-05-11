class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create adjacency list using sets, visit set
        # if we visit all nodes, true

        adj =[set() for _ in range(n)]
        visit = set()

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        q = deque([0])
        visit.add(0)
        
        while q:
            a = q.popleft()

            for b in adj[a]:
                adj[b].remove(a)
                if b in visit: 
                    return False
                
                visit.add(b)
                q.append(b)
        
        return len(visit) == n