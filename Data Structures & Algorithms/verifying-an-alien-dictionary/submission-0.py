class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dct = {}

        for i, c in enumerate(order):
            dct[c] = i
        
        for i in range(1, len(words)):
            idx1 = idx2 = 0
            w1, w2 = words[i - 1], words[i]
            while idx1 < len(w1) and idx2 < len(w2) and w1[idx1] == w2[idx2]:
                idx1, idx2 = idx1 + 1, idx2 + 1
            
            if idx1 == len(w1):
                continue
            elif idx2 == len(w2):
                return False
            
            if dct[w1[idx1]] > dct[w2[idx2]]:
                return False
        
        return True