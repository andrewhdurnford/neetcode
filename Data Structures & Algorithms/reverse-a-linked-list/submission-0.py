# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev = None
        curr = head
        nex = curr.next
        curr.next = prev
        while nex:
            prev = curr
            curr = nex
            nex = nex.next
            curr.next = prev
        return curr