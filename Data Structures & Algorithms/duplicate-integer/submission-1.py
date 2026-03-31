class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for n in nums:
            if n in new:
                return True
            new.append(n)
        return False