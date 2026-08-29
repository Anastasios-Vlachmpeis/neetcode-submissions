class Solution:
    def findMin(self, nums: List[int]) -> int:
        bot = 0
        top = len(nums) - 1

        while top > bot :
            c = bot + (top - bot) // 2
            if nums[c] < nums[top]:
                top = c
            else:
                bot = c + 1

        return nums[bot]


