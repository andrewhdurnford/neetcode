class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res, reslen = "", 0

        for i, c in enumerate(s):
            l, r = i, i
            cur = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur += 2
                
                if cur > reslen:
                    reslen = cur
                    res = s[l : r + 1]
                
                l, r = l - 1, r + 1

            l, r = i, i + 1
            cur = 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur += 2
                if cur > reslen:
                    reslen = cur
                    res = s[l : r + 1]
                
                l, r = l - 1, r + 1
        
        return res