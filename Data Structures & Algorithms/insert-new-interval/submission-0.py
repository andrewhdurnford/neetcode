class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        
        res = []

        for i, n in enumerate(intervals):
            
            if new[1] < n[0]:
                res.append(new)
                return res + intervals[i:]

            elif new[0] > n[1]:
                res.append(n)

            else:
                new = [
                    min(new[0], n[0]), 
                    max(new[1], n[1])
                    ]
        
        res.append(new)
        return res