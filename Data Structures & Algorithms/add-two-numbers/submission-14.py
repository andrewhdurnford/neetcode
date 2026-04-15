# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        i = 0

        while l1 or l2:
            # get value and iterate through list
            if l1 and l2:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
                
            # add to sum and iterate i
            total += val * (10 ** i)
            i += 1

        # create new list
        dummy = ListNode()
        cur = dummy
        total = str(total)

        for i in range(len(total) - 1, -1, -1):
            node = ListNode(total[i])
            cur.next = node
            cur = cur.next
        
        return dummy.next

