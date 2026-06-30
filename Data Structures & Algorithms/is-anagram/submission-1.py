class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k = list(s)
        print(k)
        for i in t:
            if i in k:
                k.remove(i)
            else:
                return False  
        if k:
            return False
        return True