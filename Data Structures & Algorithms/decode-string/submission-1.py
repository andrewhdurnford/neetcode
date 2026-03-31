class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):
            res = ''
            i = 0
            while i < len(s):
                
                if s[i].isdigit():
                    
                    mult = ''
                    
                    while s[i].isdigit():
                        mult += s[i]
                        i += 1
                    mult = int(mult)
                
                elif s[i] == '[':
                    
                    cur = ''
                    cnt = 1
                    i += 1
                    
                    while cnt > 0:
                        if s[i] == '[':
                            cnt += 1
                        elif s[i] == ']':
                            cnt -= 1
                        if cnt > 0:
                            cur += s[i]
                        i += 1
                    
                    res += decode(cur) * mult         
                
                else:
                    res += s[i]
                    i += 1
                
            return res
        
        return decode(s)

                    
