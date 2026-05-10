"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = defaultdict(Node)
        if not node: return None
        head = node
        q = deque([node])
        visit = set([node])

        while q:
            node = q.popleft()
            copy = nodes[node.val]
            copy.val = node.val

            for nei in node.neighbors:
                nei_copy = nodes[nei.val]
                copy.neighbors.append(nei_copy)
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
        
        return nodes[head.val]

