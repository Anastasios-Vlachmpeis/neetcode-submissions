class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(dict.fromkeys(nums))
        l = len(nums)
        t = l - 1
        b = 0

        while b < t :
            c = b + (t - b) // 2
            if nums[c] < nums[t] :
                t = c
            else :
                b = c + 1

        t = b - 1 + l
        
        while t >= b :
            c = b + (t - b) // 2
            if nums[c % l] < target :
                b = c + 1
            elif nums[c % l] > target :
                t = c - 1
            else :
                return True
        return False