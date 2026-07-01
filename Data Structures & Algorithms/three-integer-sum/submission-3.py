class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ls = {}
        for x in range(len(nums)):
            i = 0
            j = len(nums)-1
            while i < j:
                if nums[x] + nums[i] + nums[j] < 0 or x == i:
                    i += 1
                elif nums[x] + nums[i] + nums[j] > 0 or x == j:
                    j -= 1
                else:
                    l = [nums[x],nums[i],nums[j]]
                    l.sort()
                    ls[tuple(l)] = l
                    j -= 1
                    i += 1
        return list(ls.values())