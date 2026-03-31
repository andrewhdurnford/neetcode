class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
            
            if i >= len(candidates) or cur_sum >= target:
                return
            

            cur.append(candidates[i])
            backtrack(i + 1, cur, cur_sum + candidates[i])
            cur.pop()

            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            backtrack(i, cur, cur_sum)

        backtrack(0, [], 0)
        return res
