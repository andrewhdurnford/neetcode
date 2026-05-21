class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        counts = [[] for _ in range(len(nums) + 1)]
        
        for key in freq.keys():
            counts[freq[key]].append(key)
        
        res = []
        i = len(nums) - 1

        while len(res) < k:
            res.extend(counts[i])
            i -= 1

        return res[:k]
