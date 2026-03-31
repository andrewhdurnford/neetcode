class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        def bisect_left(tails, n):
            l, r = 0, len(tails) -1
            while l <= r:
                m = l + ((r - l) // 2)

                if tails[m] < n:
                    l = m + 1
                else:
                    r = m - 1                  
            
            return l
                

        for n in nums:
            if not tails or n > tails[-1]:
                tails.append(n)
            else:
                idx = bisect_left(tails, n)
                tails[idx] = n
        
        return len(tails)