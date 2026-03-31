class Node:
    def __init__ (self, left=None, right=None, key=None, val=None):
        self.left = left
        self.right = right
        self.val = val
        self.key = key
    
    def pop(self):
        self.left.right, self.right.left = self.right, self.left

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(), Node()
        self.head.right, self.tail.left = self.tail, self.head
        self.cur = 0
        self.cap = capacity
        self.keys = {}
    
    def insert(self, node):
        last = self.tail.left
        last.right, self.tail.left = node, node
        node.left, node.right = last, self.tail

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        node = self.keys[key]
        node.pop()
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].pop()
        else:
            if self.cur == self.cap:
                self.popLeft()
            else:
                self.cur += 1
        
        node = Node()
        node.key = key
        node.val = value
        self.keys[key] = node
        self.insert(node)
        
    def popLeft(self):
        LRU = self.head.right
        self.head.right, LRU.right.left = LRU.right, self.head
        del self.keys[LRU.key]