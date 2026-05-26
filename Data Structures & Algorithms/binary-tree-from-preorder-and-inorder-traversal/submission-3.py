# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for i, n in enumerate(inorder):
            idx[n] = i
        preI = 0
        
        def dfs(l, r):
            nonlocal preI
            print(preI, l, r)
            if l > r:
                return None
            
            val = preorder[preI]
            root = TreeNode(val)
            preI += 1
            root.left = dfs(l, idx[val] - 1)
            root.right = dfs(idx[val] + 1, r)
            return root
        

        return dfs(0, len(preorder) - 1)