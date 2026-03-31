class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad, dire = deque(), deque()

        for i, n in enumerate(senate):
            if n == 'R':
                rad.append(i)
            else:
                dire.append(i)
        
        n = len(senate)
        
        while rad and dire:
            if rad[0] < dire[0]:
                dire.popleft()
                rad.append(rad.popleft() + n)
            else:
                rad.popleft()
                dire.append(dire.popleft() + n)
                
        
        if not rad:
            return 'Dire'
        return 'Radiant'