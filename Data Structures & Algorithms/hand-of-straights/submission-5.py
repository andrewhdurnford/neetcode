class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = defaultdict(int)
        hand.sort()

        for c in hand:
            cnt[c] += 1
        
        for n in cnt:
            if cnt[n] == 0:
                continue
            
            while cnt[n] > 0:
                for i in range(groupSize):
                    if cnt[n + i] == 0:
                        return False
                    
                    cnt[n + i] -= 1
        
        for n in cnt:
            if cnt[n] > 0:
                return False

        return True
        
