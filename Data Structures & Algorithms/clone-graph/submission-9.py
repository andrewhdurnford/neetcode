
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        head = node
        copies = defaultdict(Node)

        q = deque([node])
        visit = set([node])

        while q:
            node = q.popleft()
            copy = copies[node]
            copy.val = node.val
            for nei in node.neighbors:
                copy.neighbors.append(copies[nei])
                if nei not in visit:
                    q.append(nei)
                    visit.add(nei)
        
        return copies[head]
        

            
        