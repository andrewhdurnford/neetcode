class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        # sChars -> all chars in s 
        # tChars -> all chars in t
        # mChars -> all chars in s that are in t
        sChars, tChars, mChars = [0] * 52, [0] * 52, [0] * 52

        # set tChars
        for c in t:
            tChars[ord(c) - ord('a')] += 1
        
        # set left pointer, initialize shortest length & result
        l = 0
        res = ""
        flag = 0

        # iterate through string
        for r, c in enumerate(s):
            # char found and char in t
            if (tChars[ord(c) - ord('a')] != 0):
                
                # increment sChars
                sChars[ord(c) - ord('a')] += 1

                # increment mChars if necessary
                if not flag and mChars[ord(c) - ord('a')] < tChars[ord(c) - ord('a')]:
                    mChars[ord(c) - ord('a')] += 1
                
                # if all chars found, set flag
                if mChars == tChars:
                    flag = 1
                
                if flag:
                    if len(res) == 0:
                        res = s[l:r+1]
                    # while char at left pointer is redundant
                    while(sChars[ord(s[l]) - ord('a')] > tChars[ord(s[l]) - ord('a')] # more than enough found
                    or tChars[ord(s[l]) - ord('a')] == 0): # not in t

                        # remove char at left pointer and iterate left pointer
                        sChars[ord(s[l]) - ord('a')] -= 1
                        l += 1

                        # check if new substring is shorter
                        if r - l + 1 < len(res):
                            res = s[l:r+1]

        return res


                