class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node (0, 0)
        self.left.right, self.right.left = self.right, self.left
    
    def insert(self, node):
        left, right = self.right.left, self.right
        left.right = right.left = node
        node.left, node.right = left, right
    
    def remove(self, node):
        left, right = node.left, node.right
        left.right, right.left = right, left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = (Node(key, value))
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.right
            self.remove(lru)
            del self.cache[lru.key]
        return None