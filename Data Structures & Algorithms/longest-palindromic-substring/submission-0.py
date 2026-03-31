class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        res = 0
        res_str = ""
        
        for i, c in enumerate(s):
            
            l, r, cur = i - 1, i + 1, 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur += 2
                l, r = l - 1, r + 1
            
            if cur > res: res_str = s[i - cur // 2 : i + cur // 2 + 1]
            res = max(res, cur)


            if i < len(s) - 1 and c == s[i + 1]:
                l, r, cur = i, i + 1, 0
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    cur += 2
                    l, r = l - 1, r + 1

            if cur > res: res_str = s[i - cur // 2 + 1 : i + cur // 2 + 1]
            res = max(res, cur)

            if i > 0 and c == s[i - 1]:
                l, r, cur = i - 1, i, 0
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    cur += 2
                    l, r = l - 1, r + 1
            
            if cur > res: res_str = s[i - cur // 2 + 1 : i + cur // 2 + 1]
            res = max(res, cur)
        
        return res_str

