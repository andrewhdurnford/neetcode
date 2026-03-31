# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = l1.val + l2.val
        head = ListNode(val % 10)
        curr = head
        val = val // 10 if val >= 10 else 0
        
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            val += l1.val + l2.val
            curr.next = ListNode(val % 10)
            curr = curr.next
            val = val // 10 if val >= 10 else 0
        
        while l1.next:
            l1 = l1.next
            val += l1.val
            curr.next = ListNode(val % 10)
            curr = curr.next
            val = val // 10 if val >= 10 else 0
        
        while l2.next:
            if l2.next:
                l2 = l2.next
                val += l2.val
            curr.next = ListNode(val % 10)
            curr = curr.next
            val = val // 10 if val >= 10 else 0
        
        while val > 0:
            curr.next = ListNode(val % 10)
            curr = curr.next
            val = val // 10 if val > 10 else 0

        
        return head
