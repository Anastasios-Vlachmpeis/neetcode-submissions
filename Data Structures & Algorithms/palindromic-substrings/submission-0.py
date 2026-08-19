class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        count = 0
        for i in range(l):

            j = i
            y = j+1
            # even case
            while j >= 0 and y < l and s[j] == s[y] :
                count += 1
                j -= 1
                y += 1
            
            j = i-1
            y = i+1
            # odd case
            while j >= 0 and y < l and s[j] == s[y] :
                count += 1
                j -= 1
                y += 1
                
            count += 1

        return count