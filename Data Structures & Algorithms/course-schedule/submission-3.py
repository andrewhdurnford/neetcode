class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for pre, course in prerequisites:
            indeg[course] += 1
            adj[pre].append(course)
        
        q = deque()

        for c in range(numCourses):
            if indeg[c] == 0:
                q.append(c)

        finish = 0
        while q:
            course = q.popleft()
            finish += 1

            for nei in adj[course]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return finish == numCourses
