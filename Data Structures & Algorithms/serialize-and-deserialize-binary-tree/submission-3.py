# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []

        def dfs(root):
            nonlocal serialized
            if not root:
                serialized.append('N')
                return

            serialized.append('V' + str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(serialized)
        return ''.join(serialized)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0

        def dfs():
            nonlocal i
            if data[i] == 'N':
                i += 1
                return None
            
            else:
                i += 1
                val = ''
                while data[i].isdigit():
                    val += data[i]
                    i += 1
            
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root
    
        return dfs()


