class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize deque and result
        deq = []
        res = []
        
        for i, n in enumerate(nums):
            # Remove item outside of window
            if deq and deq[0] <= i - k:
                deq.pop(0)
            
            # Remove numbers to the left that <= current right edge
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            
            # Add right edge
            deq.append(i)

            # If window is initialized, append to result
            if i >= k - 1:
                res.append(nums[deq[0]])
                
        return res
                