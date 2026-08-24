class Solution:
    def validPalindrome(self, s: str) -> bool:
        ls = len(s)
        for i in range(ls) :
            s1 = s[0:i] + s[i+1:ls]
            if s1 == s1[::-1] :
                return True

        return False