class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        needed = 0
        for c in t:
            if need[c] == 0:
                needed += 1
            need[c] += 1
        
        have = defaultdict(int)
        found = 0
        
        res = ""
        reslen = 1001
        l = 0
        
        for r, c in enumerate(s):
            have[c] += 1
            
            if have[c] == need[c]:
                found += 1
            
            while have[s[l]] > need[s[l]] and l < len(s) - 1:
                have[s[l]] -= 1
                l += 1

            if found == needed:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = s[l : r + 1]
        
        return res
