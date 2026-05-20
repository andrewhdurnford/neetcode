class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)) + [1 , 1]

        # at each char:
        # if from 1-9, dp[i] += dp[i + 1]
        # if from 1, or 2 and s[i + 1] from 0-6 += dp[i + 2]

        for i in range(len(s) - 1, -1, -1):
            if s[i] != '0': dp[i] += dp[i + 1]

            if (i < len(s) - 1 and 
            (s[i] == '1' or 
            s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i + 2]
        
        return dp[0]