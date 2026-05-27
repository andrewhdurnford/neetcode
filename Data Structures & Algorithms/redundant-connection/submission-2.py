class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # compute indegs
        # build adjacency lists using sets
        # prune leaves
        # start bfs with nodes with deg 1
        # remove them from their neighbors adjacency list
        # add them to set
        # if neighbors adjacency list len <= 1, add nei to q

        n = len(edges)

        deg = [0] * (n + 1)
        adj = [set() for _ in range(n + 1)]

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
            deg[a] += 1
            deg[b] += 1
        
        q = deque()
        pruned = set()

        for i in range(n + 1):
            if deg[i] == 1:
                q.append(i)
                pruned.add(i)
        
        while q:
            cur = q.popleft()
            for nei in list(adj[cur]):
                adj[nei].remove(cur)
                deg[nei] -= 1
                if deg[nei] == 1:
                    q.append(nei)
                    pruned.add(nei)
        
        for a, b in reversed(edges):
            if not a in pruned and not b in pruned:
                return [a, b]
