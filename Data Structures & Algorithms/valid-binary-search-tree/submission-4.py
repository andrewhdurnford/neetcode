# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, mini, maxi):
            if not root:
                return True
            
            if root.val <= mini or root.val >= maxi:
                return False
            
            left = dfs(root.left, mini, root.val)
            right = dfs(root.right, root.val, maxi)
            return left and right
        
        return dfs(root, -1001, 1001)