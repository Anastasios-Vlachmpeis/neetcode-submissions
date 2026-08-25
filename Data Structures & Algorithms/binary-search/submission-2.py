class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums)
        bot = 0
        i = 0 
        while i < int(len(nums) / 2 + 1) :
            c = (top + bot) // 2
            if nums[c] == target :
                return c
            elif nums[c] < target :
                bot = c
            else :
                top = c
            i += 1
        return -1