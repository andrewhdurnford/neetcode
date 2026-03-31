class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cntR, cntD = 0, 0
        n = len(senate)
        banned = [False] * n
        
        for s in senate:
            if s == 'R':
                cntR += 1
            if s == 'D':
                cntD += 1
        
        i = 0
        while True:
            if cntR == 0:
                return 'Dire'
            elif cntD == 0:
                return 'Radiant'
            
            if banned[i % n]:
                i += 1
                continue
            
            j = i + 1
            while banned[j % n] or senate[i % n] == senate[j % n]:
                j += 1
            
            banned[j % n] = True
            if senate[j % n] == 'R':
                cntR -= 1
            else:
                cntD -= 1
            i += 1
        
        