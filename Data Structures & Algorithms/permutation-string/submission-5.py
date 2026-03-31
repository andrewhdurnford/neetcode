class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0] * 26
        cur = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        l = 0
        
        for r, c in enumerate(s2):
            while cur[ord(c) - ord('a')] == need[ord(c) - ord('a')]:
                cur[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            cur[ord(c) - ord('a')] += 1
            if cur == need:
                return True

        return False

