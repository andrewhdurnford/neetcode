class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(cur, cursum, idx):
            if cursum == target:
                res.append(cur.copy())
                return

            if idx >= len(candidates) or cursum > target:
                return
            
            cur.append(candidates[idx])
            cursum += candidates[idx]
            backtrack(cur, cursum, idx + 1)
            cur.pop()
            cursum -= candidates[idx]

            idx += 1
            while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                idx += 1
            backtrack(cur, cursum, idx)

        backtrack([], 0, 0)
        return res
