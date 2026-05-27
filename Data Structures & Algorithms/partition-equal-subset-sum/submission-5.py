class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # check if the total is divisble by 2, if not return False
        # get the target = total / 2
        # initialize numSet = set()
        # then iterate over nums
        # add each value to previously found values
        # unless larger than target
        # and if we find target, return true

        total = sum(nums)
        if total % 2: return False

        target = total // 2
        numSet = set([0])

        for n in nums:
            for found in list(numSet):
                if n + found == target:
                    return True
                
                if n + found < target:
                    numSet.add(n + found)
        
        return False
