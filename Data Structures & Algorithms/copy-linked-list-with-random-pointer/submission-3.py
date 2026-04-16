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
        node_map = { None: None }
        cur = head

        while cur:
            if cur not in node_map:
                node_map[cur] = Node(0)

            if cur.next not in node_map:
                node_map[cur.next] = Node(0)

            if cur.random not in node_map:
                node_map[cur.random] = Node(0)

            copy = node_map[cur]
            copy.val = cur.val
            copy.next = node_map[cur.next]
            copy.random = node_map[cur.random]
            cur = cur.next
        
        return node_map[head]
                