class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        deq = deque()
        res = []

        for i in range(k - 1):
            while deq and deq[-1][0] < nums[i]:
                deq.pop()
            deq.append([nums[i], i])

        for r in range(k - 1, len(nums)):
            while deq and deq[0][1] < r - k + 1:
                deq.popleft()
            
            while deq and deq[-1][0] < nums[r]:
                deq.pop()
            
            deq.append([nums[r], r])
            res.append(deq[0][0])
        
        return res