class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l != 1 :    
            for i in range(l) :
                for j in range(i,l):
                    if nums[i] == nums[j] and abs(i-j) <= k and i != j:
                        return True
        
        return False
            

