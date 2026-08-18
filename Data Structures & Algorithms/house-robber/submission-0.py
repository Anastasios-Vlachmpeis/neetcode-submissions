class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = 3*[0] + nums
        l = len(nums)
        for i in range(3,l):
            nums[i] = nums[i] + max(nums[i-2],nums[i-3])

        return max(nums[l-1],nums[l-2])