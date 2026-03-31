class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            l, r = i - 1, i + 1
            cur = 1
            if cur > resLen:
                resLen = cur
                res = s[l : r + 1]

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur += 2
                if cur > resLen:
                    resLen = cur
                    res = s[l : r + 1]
                l, r = l - 1, r + 1
            
            l, r = i, i + 1
            cur = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur += 2
                if cur > resLen:
                    resLen = cur
                    res = s[l : r + 1]
                l, r = l - 1, r + 1

        return res

