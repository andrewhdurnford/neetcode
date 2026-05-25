class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indeg and adjacency list
        res = []

        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course] += 1
        
        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            res.append(course)

            for req in adj[course]:
                indeg[req] -= 1
                if indeg[req] == 0:
                    q.append(req)
        
        return res if len(res) == numCourses else []