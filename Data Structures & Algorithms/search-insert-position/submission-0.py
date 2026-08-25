class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        top = len(nums) - 1
        bot = 0

        while bot <= top :
            c = (top + bot) // 2
            if nums[c] == target :
                return c
            elif target > nums[c] :
                bot = c + 1
            else:
                top = c - 1
        return top + 1