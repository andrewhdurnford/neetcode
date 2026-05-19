class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = defaultdict(int)
        hand.sort()

        for c in hand:
            cnt[c] += 1
        
        for c in cnt.keys():
            while cnt[c] > 0:
                for i in range(c, c + groupSize):
                    if cnt[i] == 0:
                        return False
                    cnt[i] -= 1

        return True