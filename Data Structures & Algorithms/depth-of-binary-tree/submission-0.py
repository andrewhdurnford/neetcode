# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def maxDepth(self, root: Optional[TreeNode], depth=0, maxD=0) -> int:
        if not root: return maxD
        depth = depth + 1
        maxD = max(depth, maxD) 

        if root.left: 
            lD = self.maxDepth(root.left, depth, maxD)
            maxD = max(lD, maxD)
        
        if root.right:
            rD = self.maxDepth(root.right, depth, maxD)
            maxD = max(rD, maxD)


        return maxD