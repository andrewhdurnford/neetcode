# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append((root, None, None))

        while queue:
            node, lP, rP = queue.popleft()

            if node.left:
                if node.left.val < node.val and ((not lP) or node.left.val > lP):
                    queue.append((node.left, lP, node.val))
                else:
                    return False

            if node.right:
                if node.right.val > node.val and ((not rP) or node.right.val < rP):
                    queue.append((node.right, node.val, rP))
                else:
                    return False

        
        return True