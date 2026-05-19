class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        for i, j, k in triplets:
            if i <= target[0] and j <= target[1] and k <= target[2]:
                cur = [max(cur[0], i), max(cur[1], j), max(cur[2], k)]
        
        return cur == target