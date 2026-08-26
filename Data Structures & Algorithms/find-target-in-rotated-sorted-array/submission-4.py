class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        top = len(nums) - 1
        bot = 0
        ch = -1

        while top >= bot :
            c = bot + (top - bot) // 2
            if nums[c] == target :
                return c
            elif c < l - 1 and nums[c + 1] < nums[c] :
                ch = c
                break
            elif nums[bot] > nums[c] :
                top = c - 1
            else :
                bot = c + 1

        top = ch + l
        bot = ch + 1

        while top >= bot :
            
            c = bot + (top - bot) // 2
            if nums[c%l] == target :
                return c%l
            elif nums[c%l] > target :
                top = c - 1
            else :
                bot = c + 1

        return -1