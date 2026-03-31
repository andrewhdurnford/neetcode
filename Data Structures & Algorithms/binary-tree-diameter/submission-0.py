# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)

            d = lh + rh
            h = max(lh, rh) + 1
            res = max(res, d)
            return h
        
        dfs(root)

        return res
            