class Solution:
    def isNStraightHand(self, hand: List[int], g: int) -> bool:
        if len(hand) % g != 0: return False
        
        count = Counter(hand)

        # Iterate
        for n in hand:
            start = n

            # Find Group Start
            while count[start - 1]:
                start -= 1
            
            # Process All Groups Up to N
            while start <= n:

                # Process All Groups Starting With Start
                while count[start]:

                    # Process Group
                    for i in range(start, start + g):
                        if not count[i]:
                            return False
                        count[i] -= 1

                # Increment Start
                start += 1
        
        return True
