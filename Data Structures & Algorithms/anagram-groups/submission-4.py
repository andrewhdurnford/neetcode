class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            hashmap[tuple(chars)].append(s)
        
        res = []
        for k in hashmap:
            res += [hashmap[k]]

        return res
