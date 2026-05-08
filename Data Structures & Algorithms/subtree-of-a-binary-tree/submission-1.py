# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return False
            
            s = False

            if root.val == subRoot.val:
                s = same(root, subRoot)
            
            return s or dfs(root.left) or dfs(root.right)
        
        def same(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False

            left = same(p.left, q.left)
            right = same(p.right, q.right)

            return left and right and p.val == q.val
        
        return dfs(root)