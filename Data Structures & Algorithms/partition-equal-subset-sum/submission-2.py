class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        vals = set([0])
        for n in nums:
            lst = list(vals)
            for i in range(len(lst)):
                vals.add(lst[i] + n)
                if lst[i] + n == total / 2: return True
        return False