class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for n in nums:
            if n in new:
                return True
            else:
                new.add(n)
        return False