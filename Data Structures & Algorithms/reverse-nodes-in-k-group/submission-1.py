# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = Node(0, head)
        cur = head
        prevLast = dummy
        while True:
            nextFirst = cur
            for _ in range(k):
                if nextFirst:
                    nextFirst = nextFirst.next
                else:
                    return dummy.next
            
            prev = nextFirst
            curLast = cur
            # prevLast -> 0
            # nextFirst -> 4
            # cur -> 1
            # prev -> 4

            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                # nxt = 2, 1.next = 4, prev = 1, cur = 2
                # nxt = 3, 2.next = 1, prev = 2, cur = 3
                # nxt = 4, 3.next = 2, prev = 3, cur = 4
            
            prevLast.next = prev
            prevLast = curLast
        

            




        # 0, 1, 2, 3, 4 ...
        # rmb 0
        # rmb 4
        # prev = 4
        # reverse 1, 2, 3
        # 3 -> 2 -> 1 -> 4 ...
        # point 0 at 3

