class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        long = ""
        for i in range(l):
            j = i
            y = j-1
            curr = ""
            # Even case
            while j < l and y >= 0 and s[j] == s[y]:
                curr = s[y] + curr + s[j]
                y -= 1
                j += 1
            
            long = curr if len(curr) > len(long) else long 
            
            j = i-1
            y = i+1
            curr = s[i]
            # odd case
            while j >= 0 and y < l and s[j] == s[y]:
                curr = s[j] + curr + s[y]
                y += 1
                j -= 1

            long = curr if len(curr) > len(long) else long

        return long
            