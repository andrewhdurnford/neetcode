# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, cur):
            nonlocal res
            
            if not root:
                return
            
            res = max(res, cur + 1)
            dfs(root.left, cur + 1)
            dfs(root.right, cur + 1)
        
        dfs(root, 0)
        return res