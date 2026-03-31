# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge case
        if not head.next: return None

        # init dummy, set slow & fast to dummy
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
    
        # iterate fast n times
        for i in range(n):
            fast = fast.next
        
        # find end of list
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # cut out node
        slow.next = slow.next.next

        return dummy.next