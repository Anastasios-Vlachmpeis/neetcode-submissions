class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for i in nums:
            s[i] = s.get(i,0) + 1
        l = {k: v for k, v in sorted(s.items(), key=lambda item: item[1])}
        return list(l.keys())[len(l.keys())-k:]