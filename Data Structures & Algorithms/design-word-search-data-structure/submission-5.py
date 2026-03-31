class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.children = {}
        
    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.eow = True

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            nonlocal word
            
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(child, j + 1): return True
                    return False
                
                if word[j] not in cur.children:
                    return False
                cur = cur.children[word[j]]
            
            return cur.eow
        
        return dfs(self, 0)


