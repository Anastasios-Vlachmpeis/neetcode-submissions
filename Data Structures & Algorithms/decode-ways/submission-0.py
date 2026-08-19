class Solution:
    def numDecodings(self, s: str) -> int:
        d = d2 = 0
        d1 = 1
        l = len(s)
        for i in range(l - 1, -1, -1) :
            if s[i] == "0":
                d = 0
            else :
                d = d1
            
            if i + 1 < l and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456') :
                d += d2

            d, d1, d2 = 0, d, d1 

        return d1
            
            
            
