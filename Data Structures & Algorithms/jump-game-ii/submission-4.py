class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return None
        if len(nums) <= 1: return 0
        res = 1
        l = 1
        r = nums[0]

        while r < len(nums) - 1:
            res += 1
            nxt = None
            dist = 0

            for i in range(l, r + 1):
                if nums[i] + i > dist:
                    dist = nums[i] + i
                    nxt = i

            l = nxt
            r = nxt + nums[l]
        
        return res
