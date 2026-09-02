class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hs = {}
        for i in range(len(order)) :
            hs[order[i]] = i

        for i in range(len(words) - 1) :
            li = len(words[i])
            li2 = len(words[i+1])
            j = 0
            print(li,li2)
            while j < li and j < li2 :
                if hs[words[i][j]] < hs[words[i+1][j]]:
                    break
                if hs[words[i][j]] > hs[words[i+1][j]]:
                    return False
                j += 1
            print(words[i][:li2], words[i+1], words[i])
            if words[i][:li2] == words[i+1] and li > li2 :
                return False

        return True
            