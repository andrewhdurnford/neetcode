# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        queue = deque()

        queue.append((root, root.val))

        while queue:
            node, l = queue.pop()

            if node.val >= l:
                res += 1
                l = node.val
            
            if node.left: queue.append((node.left, l))
            if node.right: queue.append((node.right, l))

        return res