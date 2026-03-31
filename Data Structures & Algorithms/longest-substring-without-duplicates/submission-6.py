class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque 

        chars = set()
        l = 0
        maxL = 0

        for r, c in enumerate(s):
            while c in chars:
                chars.remove(s[l])
                l += 1
            chars.add(c)
            maxL = max(maxL, r - l + 1)

        return maxL

