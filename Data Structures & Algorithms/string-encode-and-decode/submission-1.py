class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            l = str(len(s))
            out += l + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
    
        strs = []
        i = 0

        while i < len(s):
            
            l = ""

            while s[i] != '#':
                l += s[i]
                i += 1

            l = int(l)
            i += 1
            
            strs.append(s[i:(i + l)])
            i += l
        
        return strs

            

            
            
