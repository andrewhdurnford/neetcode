class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1, t2 = text1, text2
        if len(text1) < len(text2):
            t1, t2 = text2, text1
        
        prev = [0] * (len(t2) + 1)
        cur = [0] * (len(t2) + 1)

        for i in range(len(t1) - 1, -1, -1):
            for j in range(len(t2) - 1, -1 ,-1):
                
                if t1[i] == t2[j]:
                    cur[j] = prev[j + 1] + 1
                else:
                    cur[j] = max(cur[j + 1], prev[j])
            
            cur, prev = prev, cur

        return prev[0]