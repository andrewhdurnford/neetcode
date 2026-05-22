class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = 0, 0, 0
        p, q, r = target

        for x, y, z in triplets:
            if x <= p and y <= q and z <= r:
                a = max(a, x)
                b = max(b, y)
                c = max(c, z)
            
            if a == p and b == q and c == r:
                return True
        
        return False

