# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif p and not q or q and not p or q.val != p.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def dfs(root):
            nonlocal subRoot
            if not root: return False
            same = False

            if root.val == subRoot.val:
                same = isSameTree(root, subRoot)
            
            left = dfs(root.left)
            right = dfs(root.right)

            return same or left or right
        
        return dfs(root)