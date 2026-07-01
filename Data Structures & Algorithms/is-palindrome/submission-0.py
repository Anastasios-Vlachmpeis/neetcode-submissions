import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]',"",s.lower())
        return s == s[::-1]