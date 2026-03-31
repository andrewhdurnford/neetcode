class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            cnt[n] += 1

        for n, c in cnt.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(res) < k:
                    res.append(n)
            
        return res