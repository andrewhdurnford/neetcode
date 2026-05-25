class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s))

        for i in range(0, len(s)):
            if i == 0 or dp[i - 1]:
                for w in wordDict:
                    if (i + len(w) - 1 < len(s) and 
                    s[i: i + len(w)] == w):
                        dp[i + len(w) - 1] = True

        return dp[-1]

