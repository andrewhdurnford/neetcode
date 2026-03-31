class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize window
        deq = []
        for i in range(k):
            if not deq or nums[deq[-1]] > nums[i]:
                deq.append(i)
            else:
                while (deq and nums[deq[-1]] <= nums[i]):
                    deq.pop()
                deq.append(i)
        
        res = [nums[deq[0]]]
        
        for i in range(k, len(nums)):
            if deq and deq[0] <= i - k:
                deq.pop(0)
            
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)

            res.append(nums[deq[0]])
        return res
                