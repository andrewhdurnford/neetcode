class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()

        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(c):
            if c in path:
                return False
            
            if preMap[c] == []:
                return True

            path.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            path.remove(c)
            preMap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True