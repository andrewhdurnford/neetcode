class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, cur, res = 0, 0, 0, 100001

        for r in range(len(nums)):
            cur += nums[r]

            while cur >= target:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
        
        return res if res < 100001 else 0