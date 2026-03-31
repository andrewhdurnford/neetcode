# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        v = 0

        def dfs(root):
            nonlocal v
            if not root:
                return None

            l = dfs(root.left)
            if l: return l

            v += 1
            if v == k: return root.val

            r = dfs(root.right)
            if r: return r
            
        return dfs(root)
