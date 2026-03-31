class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(k - 1):
            while q and q[-1][0] < nums[i]:
                q.pop()
            
            q.append([nums[i], i])

        
        for i in range(k - 1, len(nums)):
            while q and q[-1][0] < nums[i]:
                q.pop()

            if q and q[0][1] <= i - k:
                q.popleft()
            
            q.append([nums[i], i])
            
            res.append(q[0][0])

        return res