class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        
        nums1 = 2*[0] + nums
        nums1[2] = 0
        l = len(nums1)
        nums2 = 2*[0] + nums
        nums2[l-1] = 0

        for i in range(3,l):
            nums1[i] = nums1[i] + max(nums1[i-2],nums1[i-3])
        for i in range(3,l):
            nums2[i] = nums2[i] + max(nums2[i-2],nums2[i-3])

        return max(nums2[l-1],nums2[l-2],nums1[l-1],nums1[l-2])