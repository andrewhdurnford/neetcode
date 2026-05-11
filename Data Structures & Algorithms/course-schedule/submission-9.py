class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # just track indegs and adjacency list
        
        indeg = [0] * numCourses
        deps = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indeg[course] += 1
            deps[pre].append(course)

        q = deque()
        
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        taken = 0

        while q:
            taken += 1
            course = q.popleft()
            for c in deps[course]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    q.append(c)
        
        return taken == numCourses
