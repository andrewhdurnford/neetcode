class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 1
        
        for i in range(len(s) - 1, -1, -1):
            dp = 0
            if s[i] in '123456789':
                dp += dp1
            
            if i < len(s) - 1  and (s[i] == '1' or 
            s[i] == '2' and 
            s[i + 1] in '0123456'):
                dp += dp2
            
            dp1, dp2 = dp, dp1
        
        return dp
            