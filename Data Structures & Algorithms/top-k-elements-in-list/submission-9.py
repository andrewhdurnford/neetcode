class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)

        for n in nums:
            cnt[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, v in cnt.items():
            freq[v].append(n)
        
        
        res = []
        for i in range(len(nums), -1, -1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)
        
        return res