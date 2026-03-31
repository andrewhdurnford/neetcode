class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        length = len(nums)
        res = []

        for i, n in enumerate(sortedNums):
            
            if i > 0 and n == sortedNums[i - 1]:
                continue

            target = - n
            l = i + 1
            r = length - 1
            while l < r:
                summ = sortedNums[l] + sortedNums[r]

                if summ == target:
                    res.append([n, sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1
                    while sortedNums[l] == sortedNums[l - 1] and l < r:
                        l += 1

                elif summ < target:
                    l += 1
                else:
                    r -= 1

        return res
            

