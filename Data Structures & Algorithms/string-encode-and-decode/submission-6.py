class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '*' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = ""
            while s[i] != '*':
                l += s[i]
                i += 1
            l = int(l)
            i += 1
            res.append(s[i: l + i])
            i = l + i
        return res
            