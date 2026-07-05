class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = set(nums)
        nn = list(n)
        nn.sort()
        longSeq = 1
        runnSeq = 1
        
        for i in range(len(nn)-1):
            if nn[i] + 1 == nn[i + 1]:
                runnSeq += 1
            else :
                longSeq = max(longSeq,runnSeq)
                runnSeq = 1
        return max(longSeq,runnSeq)