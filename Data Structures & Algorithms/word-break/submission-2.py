class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            if dp[i + 1]:
                for w in wordDict:
                    if (i - len(w) + 1 >= 0 and 
                    s[i - len(w) + 1: i + 1] == w):
                        dp[i - len(w) + 1] = True
        
        return dp[0]

