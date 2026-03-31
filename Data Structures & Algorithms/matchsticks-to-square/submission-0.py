class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = sum(matchsticks)
        if n % 4 != 0: return False
        length = n // 4
        matchsticks.sort(reverse=True)
        
        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for s in range(4):
                if sides[s] + matchsticks[i] <= length:
                    sides[s] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[s] -= matchsticks[i]
                
                if sides[s] == 0:
                    break


            return False
        
        return dfs(0)


