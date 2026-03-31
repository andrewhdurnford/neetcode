class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        for tout, tin in trust:
            outdeg[tout] += 1
            indeg[tin] += 1
        
        for i in range(1, n + 1):
            if outdeg[i] == 0 and indeg[i] == n - 1:
                return i
        return -1