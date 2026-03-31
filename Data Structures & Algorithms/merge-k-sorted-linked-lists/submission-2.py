# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        heap = []
        heapq.heapify(heap)
        cnt = 0

        for l in lists:
            if l: heapq.heappush(heap, (l.val, cnt, l))
            cnt += 1
        
        head = heapq.heappop(heap)[2]
        if head.next: heapq.heappush(heap, (head.next.val, cnt, head.next))
        cnt += 1
        cur = head

        while heap:
            node = heapq.heappop(heap)[2]
            print(node.val)
            cur.next = node
            cur = cur.next
            if node.next: heapq.heappush(heap, (node.next.val, cnt, node.next))
            cnt += 1

        return head


        