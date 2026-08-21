class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # Works, just is too slow
        cache = (target + 1) * [0]

        def rec(curr: int) :
            if curr == target :
                return 1 
            ways = 0
            for i in nums :
                if curr + i <= target :
                    if cache[curr + i] == 0 :
                        ways += rec(curr + i)
                        cache[curr + i] = rec(curr + i)
                    else :
                        ways += cache[curr + i]
            return ways

        return rec(0)
