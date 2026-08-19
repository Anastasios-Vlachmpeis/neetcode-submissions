class Solution:
    def tribonacci(self, n: int) -> int:
        ca = (n+1)*[-1]
        def rec(i) :
            if i <= 0:
                return 0
            elif i <= 2:
                return 1
            if ca[i] != -1:
                return ca[i]
            ca[i] = rec(i-1) + rec(i-2) + rec(i-3)
            return ca[i]
        return rec(n)