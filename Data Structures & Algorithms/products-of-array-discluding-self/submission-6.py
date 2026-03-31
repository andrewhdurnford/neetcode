class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0
        res = []

        for n in nums:
            if n != 0:
                product *= n
            else:
                zeroes += 1
        
        if zeroes > 1: return [0] * len(nums)

        for n in nums:
            if zeroes > 0 and n != 0:
                res.append(0)
                continue
            
            if n == 0:
                res.append(product)
            else:
                res.append(int(product / n))
        
        return res

