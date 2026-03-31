class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.eow = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()

        for w in dictionary:
            trie.insert(w)
        
        dp = {}
        dp[len(s)] = 0

        def dfs(i):
            if i in dp: return dp[i]
            
            res = 1 + dfs(i + 1)

            cur = trie.root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.eow: res = min(res, dfs(j + 1))

            dp[i] = res
            return res
        
        return dfs(0)