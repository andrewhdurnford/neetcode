class Node:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.vals = defaultdict(int)
        self.capacity = capacity
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): 
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.vals:
            node = self.vals[key]
            self.remove(node)
            self.insert(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.vals:
            self.remove(self.vals[key])
        
        self.vals[key] = Node(key, value)
        self.insert(self.vals[key])

        if len(self.vals) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.vals[lru.key]

        

