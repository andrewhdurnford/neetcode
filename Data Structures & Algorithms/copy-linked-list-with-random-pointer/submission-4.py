# Definition for a Node.
class Node:
    def __init__(self, val: int = None, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = defaultdict(Node)
        cur = head
        copy[None] = None

        while cur:
            copy[cur].val = cur.val
            copy[cur].next = copy[cur.next]
            copy[cur].random = copy[cur.random]
            cur = cur.next
        
        return copy[head]
