class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = len(s) 
        if ls <= 1 :
            return ls
        st = set()
        lind = 0
        l = s[lind]
        st.add(l)
        ml = 1

        for i in range(1,ls) :
            
            while s[i] in st :
                st.remove(l)
                lind += 1
                l = s[lind]
            
            
            st.add(s[i])
            ml = max(ml, len(list(st)))
            
        return ml
            
