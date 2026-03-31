class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newnums = []
        for i in nums:
            if i in newnums:
                return True
            newnums.append(i)
        return False