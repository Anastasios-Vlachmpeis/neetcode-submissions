class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums) - 1
        bot = 0
        while bot <= top :
            c = (top + bot) // 2
            if nums[c] == target :
                return c
            elif nums[c] < target :
                bot = c + 1
            else :
                top = c - 1
        return -1