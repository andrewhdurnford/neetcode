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
        visit = set([node.val])
        
        while q:
            node = q.popleft()
            nodes[node.val].val = node.val

            for nei in node.neighbors:
                nodes[node.val].neighbors.append(nodes[nei.val])
                if nei.val not in visit:
                    visit.add(nei.val)
                    q.append(nei)
        
        return nodes[head.val]


