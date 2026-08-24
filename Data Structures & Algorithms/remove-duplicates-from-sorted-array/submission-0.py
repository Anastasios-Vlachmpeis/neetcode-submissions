class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 0
        while i < len(nums)-1 :
            if nums[i] == nums[i+1] :
                nums.remove(nums[i])
            else :
                i += 1
        nums.sort()
        
        return len(nums)