# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        # Find midpoint
        slow = fast = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        # Disconnect from second half
        prev.next = None
        
        # Reverse second half
        prev = None
        cur = slow

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp


        # Merge lists
        cur = dummy
        h1 = head
        h2 = prev

        while h1 and h2:
            cur.next = h1
            h1 = h1.next
            cur = cur.next
            cur.next = h2
            h2 = h2.next
            cur = cur.next
        
        if h2:
            cur.next = h2
        
        
        
            
