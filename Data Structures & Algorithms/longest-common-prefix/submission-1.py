class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        
        l = float('inf')

        for i in range(len(strs)):
            l = min(l, len(strs[i]))

        if l == 0:
            return ''

        c = strs[0][0]

        for i in range(l):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return pre
            pre += c
        
        return pre