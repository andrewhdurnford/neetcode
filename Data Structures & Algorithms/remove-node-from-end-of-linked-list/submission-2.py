# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Null check
        if not head or not head.next: return None

        # Get length
        length = -n
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Catch first node removal case
        if length == 0: return head.next
        curr = head

        for _ in range(length - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head
        