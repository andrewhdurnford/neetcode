class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        t = n * 2

        def gen(s, o, c):
            print(s)
            if o == n:
                while len(s) < t:
                    s += ')'
                if s not in res:
                    res.add(s)
                

            else:
                if o - c > 0:
                    gen((s + ')'), o, c + 1)
                gen((s + '('), o + 1, c)
        
        gen('', 0, 0)
            
        return list(res)
