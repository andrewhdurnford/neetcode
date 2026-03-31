class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        node = self.head
        for i in range(index):
            if node.next_node:
                node = node.next_node
            else:
                return -1
        return node.val if node else -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head: 
            self.head = new_node
            return
        node = self.head
        while node.next_node:
            node = node.next_node
        
        node.next_node = new_node

    def remove(self, index: int) -> bool:
        if not self.head: return False
        node = self.head

        if index == 0:
            self.head = self.head.next_node
            return True
        
        for i in range(index - 1):
            if node.next_node:
                node = node.next_node
            else: return False
        
        if not node.next_node: return False
        node.next_node = node.next_node.next_node
        return True

    def getValues(self) -> List[int]:
        if not self.head: return []
        node = self.head
        li = [node.val]
        while node.next_node:
            node = node.next_node
            li.append(node.val)
        return li
    
