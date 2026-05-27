# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        i = 0
        for node in lists:
            heapq.heappush(heap, [node.val, i, node])
            i += 1
        
        dummy = ListNode()
        prev = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            prev.next = node
            prev = node
            if node.next:
                heapq.heappush(heap, [node.next.val, i, node.next])
                i += 1
        
        return dummy.next

