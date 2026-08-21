class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        l = len(nums)
        m1 = cache = nums[0]

        for i in range(1,l) :
            mul1 = nums[i-1] * nums[i]
            if cache != 0:
                mul2 = cache * nums[i]
            else :
                mul2 = nums[i]
            cache = mul2

            m2 = max(nums[i],m1)
            m1 = max(mul1,m1)
            m1 = max(mul2,m1)

        m2 = cache = nums[l-1]

        for i in range(l-2,0,-1) :
            mul1 = nums[i+1] * nums[i]
            if cache != 0:
                mul2 = cache* nums[i]
            else :
                mul2 = nums[i]
            cache = mul2

            m2 = max(nums[i],m2)
            m2 = max(mul1,m2)
            m2 = max(mul2,m2)

        return max(m1,m2)
            