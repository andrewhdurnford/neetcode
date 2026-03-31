class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for n in nums:
            count[n] += 1
        
        for key in count:
            freq[count[key]].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            if len(res) < k:
                res.extend(freq[i])
            else:
                return res
        
        return res

        
        