# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []

        def dfs(root):
            if not root:
                s.append('N')  
                return
            
            s.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        s = '*'.join(s)
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split('*')
        i = 0
        print(data)

        def dfs():
            nonlocal i
            if data[i] == 'N':
                i += 1
                return None

            root = TreeNode(int(data[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
