class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        m = {} 
        for i in strs:
            k = str(sorted(i)) 
            m.setdefault(k,[]).append(i)
        return list(m.values())