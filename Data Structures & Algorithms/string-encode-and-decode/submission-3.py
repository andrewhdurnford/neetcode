class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            l = ""
            
            while s[i] != "#":
                l += s[i]
                i += 1
            
            l = int(l)
            res.append(s[i + 1:i + l + 1])
            i += l + 1
            
        return res

        