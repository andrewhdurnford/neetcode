class Solution:
    def numDecodings(self, s: str) -> int:
        
        valid = set(range(1, 27))
        res = []

        def dfs(i, cur):
            if i == len(s):
                if int(cur[-1]) in valid:
                    res.append(cur.copy())
                return
            
            if int(s[i]) in valid:
                cur.append(s[i])
                dfs(i + 1, cur)
                cur.pop()        

            if cur and int(cur[-1] + s[i]) in valid:
                cur[-1] += s[i]
                dfs(i + 1, cur)
                cur[-1] = cur[-1][:-1]
        
        dfs(0, [])
        return len(res)
            
