class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        count = start = 0
        while count < n:
            cur = start
            prev = nums[cur]

            while True:
                idx = (cur + k) % n
                nums[idx], prev = prev, nums[idx]
                cur = idx
                count += 1
            
                if start == cur:
                    break
            
            start += 1