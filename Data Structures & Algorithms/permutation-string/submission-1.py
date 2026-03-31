class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        s1Chars, s2Chars = [0] * 26, [0] * 26
        for c in s1:
            s1Chars[ord(c) - ord('a')] += 1

        for r, c in enumerate(s2):
            

            # Check if character in string
            if (s1Chars[ord(c) - ord('a')] == 0):
                if len(s2) - r < len(s1): return False
                l = r + 1
                s2Chars = [0] * 26
                continue

            # If char in string but amount has already been found
            # Slide window right until after first occurence
            if (s1Chars[ord(c) - ord('a')] == s2Chars[ord(c) - ord('a')]):
                while s2[l] != c:
                    s2Chars[ord(s2[l]) - ord('a')] -= 1
                    l += 1
                l += 1
                continue

            # If char in string and amount not found, add
            s2Chars[ord(c) - ord('a')] += 1
            if s1Chars == s2Chars: return True
        return False
            
