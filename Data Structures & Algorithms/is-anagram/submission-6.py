class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t): return False
        sChars, tChars = [0] * 26, [0] * 26
        for i in range(len(s)):
            sChars[ord(s[i]) - ord('a')] += 1
            tChars[ord(t[i]) - ord('a')] += 1
        return sChars == tChars