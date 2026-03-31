# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            nonlocal res
            if node:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                res.append('n')

        
        dfs(root)
        return ','.join(res)
        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split(',')
        i = 0

        def dfs():
            nonlocal i, tree
            if tree[i] == 'n':
                i += 1
                return
            else:
                val = int(tree[i])
                i += 1
                node = TreeNode(val)
                node.left = dfs()
                node.right = dfs()
                return node
        
        return dfs()

