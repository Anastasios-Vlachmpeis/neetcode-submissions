from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        indexcount = defaultdict(int)
        maxcount = 0
        for i in range(len(s)) :
            if s[i] not in index.keys() :
                index[s[i]] = i
                indexcount[i] = 1 if i == 0 else indexcount[i-1] + 1
                maxcount = max(maxcount, indexcount[i])
                continue

            pindex = index[s[i]]

            if i - pindex > indexcount[i-1] :
                indexcount[i] = indexcount[i-1] + 1
            else :
                indexcount[i] = i - pindex
            index[s[i]] = i
            maxcount = max(maxcount, indexcount[i])

        return maxcount
        