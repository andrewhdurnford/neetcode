class Node:
    def __init__(self, value=0, nxt=None, prev=None):
        self.val = value
        self.next = nxt
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = Node(val, self.right, self.right.prev)
        self.map[val] = node
        self.right.prev = node.prev.next = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            node.prev.next, node.next.prev = node.next, node.prev
            del self.map[val]
    
    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res
    
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.cnt = 0
        self.cntMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)
    
    def count(self, key):
        cnt = self.cntMap[key]
        self.cntMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.cnt and self.listMap[cnt].length() == 0:
            self.cnt += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.count(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.cache and len(self.cache) == self.cap:
            res = self.listMap[self.cnt].popLeft()
            self.cache.pop(res)
            self.cntMap.pop(res)

        self.cache[key] = value
        self.count(key)
        self.cnt = min(self.cnt, self.cntMap[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)