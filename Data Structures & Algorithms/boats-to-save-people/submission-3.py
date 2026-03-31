class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        l, r = 0, len(people) - 1
        people.sort()

        while l <= r:
            cur = limit - people[r]
            if cur - people[l] >= 0:
                l += 1
            
            r -= 1
            res += 1
        
        return res
