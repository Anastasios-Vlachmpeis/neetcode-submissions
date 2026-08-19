class Solution:
    def numDecodings(self, s: str) -> int:
        d = d2 = 0
        d1 = 1
        l = len(s)

        for i in range(l - 1, -1, -1) : #go throuhg string backwards
            print(s[i])
            if s[i] == "0": #if i current char == 0, then count at it's index is 0
                d = 0
            else :
                d = d1 #otherwise inherit previous index count
            
            if i + 1 < l and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456') :
                # if not at edge and this + prev inside [10,26], add the 2nd index's count
                d += d2 
            print(d, d1, d2)
            d, d1, d2 = 0, d, d1 #move indices 1 to the right
            print(d, d1, d2)
        return d1 #return curr count
            
            
            
