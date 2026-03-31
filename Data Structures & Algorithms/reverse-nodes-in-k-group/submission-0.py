# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node, k):
            for i in range(k):
                if node:
                    node = node.next                
            return node

        dummy = ListNode(0)
        dummy.next = head
        prevLast = dummy

        while True:
            kth = getKth(prevLast, k)
            if not kth:
                return dummy.next

            nextFirst = kth.next

            prev, cur = nextFirst, prevLast.next
            
            while cur != nextFirst:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            tmp = prevLast.next
            prevLast.next = kth
            prevLast = tmp
        
            



            


            

