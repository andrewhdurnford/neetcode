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
        nodes = defaultdict(lambda: Node(0))
        nodes[None] = None

        cur = head
        
        while cur:
            nodes[cur].val = cur.val
            nodes[cur].random = nodes[cur.random]
            nodes[cur].next = nodes[cur.next]
            cur = cur.next
        
        return nodes[head]