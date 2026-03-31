class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        res = 0
        l = 0
        common = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            common = max(common, count[s[r]])

            while(r - l + 1) - common > k:
                count[s[l]] -= 1
                common = max(common, count[s[r]])
                l += 1
            res = max(res, r - l + 1)
        return res

            