class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        neis = [[] for _ in range(numCourses)]
        
        for req, pre in prerequisites:
            neis[pre].append(req)
            indeg[req] += 1

        q = deque()
        res = 0
        
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
                res += 1
        
        while q:
            cur = q.popleft()
            
            for nei in neis[cur]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
                    res += 1
        
        return res == numCourses

















