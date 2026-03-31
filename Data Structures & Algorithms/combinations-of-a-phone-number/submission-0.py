class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []
        convert = {
            2: ('a', 'b', 'c'),
            3: ('d', 'e', 'f'),
            4: ('g', 'h', 'i'),
            5: ('j', 'k', 'l'),
            6: ('m', 'n', 'o'),
            7: ('p', 'q', 'r', 's'),
            8: ('t', 'u', 'v'),
            9: ('w', 'x', 'y', 'z')
        }

        res_set = set()

        def dfs(s, i):
            if i == len(digits):
                res_set.add(s)
                return
            
            for c in convert[int(digits[i])]:
                dfs(s + c, i + 1)
            
        dfs("", 0)
        return list(res_set)
