class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        cnt = defaultdict(int)
        hand.sort()

        for c in hand:
            cnt[c] += 1
        
        for c in cnt.keys():
            if cnt[c] > 0:
                n = cnt[c]
                for i in range(c, c + groupSize):
                    cnt[i] -= n
                    if cnt[i] < 0:
                        return False

        return True