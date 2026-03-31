class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        curr_dp = defaultdict(int)
        curr_dp[0] = 1

        for n in nums:
            next_dp = defaultdict(int)
            
            for summ, cnt in curr_dp.items():
                next_dp[summ - n] += cnt
                next_dp[summ + n] += cnt

            curr_dp = next_dp
            
        return curr_dp[target]