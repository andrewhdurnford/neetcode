# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Null check
        if not head: return None
        if not head.next: return None
        
        # Count list length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        half = length - (length // 2)

        # Split list
        curr = head
        for _ in range(half - 1):
            curr = curr.next
        
        curr2 = curr.next
        curr.next = None
        curr = head

        # Reverse list2
        prev = None
        next2 = curr2.next
        while curr2:
            curr2.next = prev
            prev = curr2
            curr2 = next2
            if next2: next2 = next2.next
        
        curr2 = prev

        # Merge lists
        while curr2:
            n1, n2 = curr.next, curr2.next
            curr.next = curr2
            curr2.next = n1
            curr, curr2 = n1, n2


