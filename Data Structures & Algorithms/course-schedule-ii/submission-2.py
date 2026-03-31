class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = set()
        cycle = set()
        res = []

        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(c):
            if c in cycle:
                return False
            if c in path:
                return True
            
            cycle.add(c)

            
            for p in preMap[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            path.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

                