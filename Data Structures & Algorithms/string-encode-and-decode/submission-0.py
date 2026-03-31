class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ";" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        while len(s) > 0:
            length = int(s[0:s.index(";")])
            decoded.append(s[s.index(";") + 1:(s.index(";") + length) + 1])
            s = s[(s.index(";") + length) + 1:]
        return decoded
