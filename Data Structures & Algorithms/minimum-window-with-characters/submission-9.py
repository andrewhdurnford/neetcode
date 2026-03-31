class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for c in t:
            countT[c] += 1
        
        have, need = 0, len(countT)
        l = 0
        res = ""
        minL = 1001

        for r, c in enumerate(s):
            if not countS and countT[c] == 0:
                continue
            
            countS[c] += 1

            if countT[c] > 0 and countS[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < minL:
                    res = s[l : r + 1]
                    minL = r - l + 1
                
                countS[s[l]] -= 1

                if countT[s[l]] > 0 and countS[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
            
        return res