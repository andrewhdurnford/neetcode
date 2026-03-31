class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res_set = set()

        def isP(s):
            return s == s[::-1]

        def dfs(cur, end, i):
            if i == len(s):
                if end == "":
                    res_set.add(tuple(cur))
                return

            end += (s[i])
            print(cur, end)
            if isP(end):
                cur.append(end)
                dfs(cur, "", i + 1)
                cur.pop()
            dfs(cur, end, i + 1)
        
        dfs([], "", 0)
        res = []
        for r in res_set:
            res.append(list(r))
        
        return res
