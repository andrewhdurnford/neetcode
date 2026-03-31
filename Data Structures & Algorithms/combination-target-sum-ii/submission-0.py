class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res_set = set()

        def dfs(i, cur, total):
            if total == target:
                res_set.add(tuple(cur.copy()))
                return
            elif i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        res = []
        for r in res_set:
            res.append(list(r))
        return res