class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # just track indegs and adjacency list
        
        indeg = [0] * numCourses
        deps = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indeg[course] += 1
            deps[pre].append(course)

        stack = []
        
        for i in range(numCourses):
            if indeg[i] == 0:
                stack.append(i)
        
        taken = 0
        res = []

        while stack:
            taken += 1
            course = stack.pop()
            res.append(course)
            for c in deps[course]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    stack.append(c)
        
        return res if taken == numCourses else []     