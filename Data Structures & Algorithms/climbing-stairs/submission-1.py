class Solution:
    
    def climbStairs(self, n: int) -> int:
        it = 0
        stor = [-1] * n

        def rec(it:int) -> int:
            if it >= n-1 :
                return 1
            if stor[it] != -1 :
                return stor[it]
            stor[it] = rec(it + 1) + rec(it + 2)
            return stor[it]
        return rec(it)
            