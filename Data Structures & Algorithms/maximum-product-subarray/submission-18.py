class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = curMax = 1
        res = -11
        for n in nums:
            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)
            res = max(curMax, curMin, res)
            print(n, curMax, curMin, res)

        return res

