class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        x, y, z = target
        for i, j, k in triplets:
            if (i <= x and j <= y and k <= z):
                cur = [max(cur[0], i), max(cur[1], j), max(cur[2], k)]

            if cur == target: return True
        
        return False