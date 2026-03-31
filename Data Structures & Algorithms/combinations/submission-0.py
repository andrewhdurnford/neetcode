class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return

            if i == n + 1:
                return
            
            backtrack(i + 1, cur)
            cur.append(i)
            backtrack(i + 1, cur)
            cur.pop()

        backtrack(1, [])
        return res