class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        cur = 0

        for i in range(len(s)):
            l = r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > cur:
                    res = s[l : r + 1]
                    cur = r - l + 1
                l, r = l - 1, r + 1
            
            l, r = i - 1, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > cur:
                    res = s[l : r + 1]
                    cur = r - l + 1
                l, r = l - 1, r + 1
        
        return res
            