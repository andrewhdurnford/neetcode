class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(cur, i):
            if i == len(word):
                return cur.eow
            
            if word[i] == '.':
                for c in cur.children:
                    if dfs(cur.children[c], i + 1):
                        return True
                return False
            
            else:
                if word[i] in cur.children:
                    return dfs(cur.children[word[i]], i + 1)
                return False

        return dfs(cur, 0)