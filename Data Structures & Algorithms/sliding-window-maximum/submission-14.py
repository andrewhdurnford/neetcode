class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()
        res = []

        for i, n in enumerate(nums):
            
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            while dq and nums[dq[-1]] <= n:
                dq.pop()

            dq.append(i)
            if k - 1 <= i:
                res.append(nums[dq[0]])
        
        return res

