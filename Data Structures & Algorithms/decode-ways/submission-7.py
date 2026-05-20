class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1: 
            if s[0] == '0': return 0
            return 1

        dp = [0] * (len(s))

        # at each char:
        # if from 1-9, dp[i] += dp[i + 1]
        # if from 1, or 2 and s[i + 1] from 0-6 += dp[i + 2]

        if s[0] == '0': return 0
        dp[0] = 1
        if s[0] == '1' or s[0] == '2' and s[1] in '0123456':
            dp[1] = 1
        if s[1] != '0': dp[1] += 1


        for i in range(2, len(s)):
            if s[i] != '0': dp[i] += dp[i - 1]

            if (s[i - 1] == '1' or 
            s[i - 1] == '2' and s[i] in '0123456'):
                dp[i] += dp[i - 2]
        
        return dp[-1]