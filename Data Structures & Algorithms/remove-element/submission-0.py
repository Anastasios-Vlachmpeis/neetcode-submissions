class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = nums.count(val)
        l = len(nums)
        for i in range(c) :
            nums.remove(val)
            
        return l - c
