class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.eow = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        
        res = []

        def dfs(i, cur, word):
            if i == len(s):
                if len(word) == 0:
                    res.append(' '.join(cur))
                return
            
            node = trie.root
            print(0)
            while i < len(s) and s[i] in node.children:
                
                node = node.children[s[i]]
                word += s[i]

                if node.eow:
                    cur.append(word)
                    print(cur)
                    dfs(i + 1, cur, '')
                    cur.pop()
                
                i += 1
                
        
        dfs(0, [], '')

        return res
