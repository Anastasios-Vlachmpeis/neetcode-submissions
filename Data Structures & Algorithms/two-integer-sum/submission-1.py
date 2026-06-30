class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = list(nums)
        for i in range(len(nums)):
            if target - nums[i] in s and nums.index(target - nums[i]) != i :
                return [min(i,nums.index(target - nums[i])),max(i,nums.index(target - nums[i]))]
        return []