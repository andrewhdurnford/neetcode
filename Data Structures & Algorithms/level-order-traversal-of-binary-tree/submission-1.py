# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue = deque()
        queue.append(root)

        while queue: 
            
            i = len(queue)
            level = []
            
            for j in range(i):
                node = queue.popleft()

                if not node:
                    continue
                
                level.append(node.val)
                queue.extend([node.left, node.right])
                
            if len(level) > 0:
                res.append(level)

        return res


