class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                return root.word 

            char = word[i]
            
            if char == '.':
                for c in root.children.values():
                    if dfs(c, i + 1):
                        return True
            
            elif word[i] in root.children:
                return dfs(root.children[word[i]], i + 1)
            
            return False
        
        return dfs(self.root, 0)
