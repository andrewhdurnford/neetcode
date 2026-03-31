# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        dummy = ListNode()
        dummy.next = head
        prevLeft, cur = dummy, head

        for _ in range(left - 1):
            prevLeft, cur = cur, cur.next
        
        
        prev = None
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        
        prevLeft.next.next = cur
        prevLeft.next = prev

        return dummy.next
        
