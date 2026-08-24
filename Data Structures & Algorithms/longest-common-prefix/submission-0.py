class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = strs[0]
        for i in strs :
            j = 0
            while j < len(i) and j < len(st) and st[j] == i[j] :
                j += 1

            st = st[:j]


        return st
