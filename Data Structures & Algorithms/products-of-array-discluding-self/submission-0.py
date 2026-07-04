class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums) 
        numL = [1] * l
        numR = [1] * l
        numF = [0] * l
        numL[0] = nums[0]
        numR[l-1] = nums[l-1]

        for i in range(1,l):
            numL[i] = nums[i]*numL[i-1]
        print(numL)
        for i in reversed(range(l-1)):
            numR[i] = numR[i+1]*nums[i] 
        print(numR)

        numF[0] = numR[1]
        numF[l - 1] = numL[l - 2]
        print(numF)

        for i in range(1,l-1):
            numF[i] = numL[i-1] * numR[i+1]
        
        return numF

