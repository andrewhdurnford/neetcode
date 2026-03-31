"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        nodes = defaultdict(lambda: Node(0))
        nodes[None] = None
        
        cur = head
        while cur:
            nodes[cur].val = cur.val
            nodes[cur].next = nodes[cur.next]
            nodes[cur].random = nodes[cur.random]
            cur = cur.next
        return nodes[head]
