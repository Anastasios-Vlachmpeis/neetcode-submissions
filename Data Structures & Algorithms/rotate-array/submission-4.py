class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l if k >= l else k
        #print(k)
        i = 0
        #print(i)
        for j in range(k, l) :
            curr = nums[i]
            nums.remove(nums[i])
            nums.append(curr)