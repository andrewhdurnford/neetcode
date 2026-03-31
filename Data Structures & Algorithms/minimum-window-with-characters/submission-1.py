class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        sChars, tChars, mChars = [0] * 52, [0] * 52, [0] * 52
        for c in t:
            tChars[ord(c) - ord('a')] += 1
        l = 0
        shortest = None
        res = ""

        for r, c in enumerate(s):
            # no chars found and char not in t
            if (tChars[ord(c) - ord('a')] == 0 and mChars == [0] * 26):
                l = r + 1
                continue
            
            # char found and char in t
            if (tChars[ord(c) - ord('a')] != 0):
                # increment
                sChars[ord(c) - ord('a')] += 1
                if mChars[ord(c) - ord('a')] < tChars[ord(c) - ord('a')]:
                    mChars[ord(c) - ord('a')] += 1
                
                if mChars == tChars:
                    if not shortest:
                        shortest = r - l + 1
                        res = s[l:r+1]
                    while(sChars[ord(s[l]) - ord('a')] > tChars[ord(s[l]) - ord('a')] # more than enough found
                    or tChars[ord(s[l]) - ord('a')] == 0): # not in t
                        print(s[l])
                        sChars[ord(s[l]) - ord('a')] -= 1
                        l += 1
                        if r - l + 1 < shortest:
                            shortest = r - l + 1
                            res = s[l:r+1]

        return res


                