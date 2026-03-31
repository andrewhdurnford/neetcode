# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        heapq.heapify(heap)
        count = 0

        for i in lists:
            if i:
                heapq.heappush(heap, (i.val, count, i))
                count += 1 # differentiate nodes with same val

        head = ListNode(0)
        prev = head

        while heap:
            cur = heapq.heappop(heap)[2]
            prev.next = cur
            prev = cur
            
            if cur.next:
                heapq.heappush(heap, (cur.next.val, count, cur.next))
                count += 1
        
        return head.next
            