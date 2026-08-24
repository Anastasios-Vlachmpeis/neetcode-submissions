class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        i = 0
        word3 = ""
        while i < w1 and i < w2 :
            word3 += word1[i] + word2[i]
            i += 1
        while i < w1:
            word3 += word1[i]
            i += 1
        while i < w2 :
            word3 += word2[i]
            i += 1
        
        return word3