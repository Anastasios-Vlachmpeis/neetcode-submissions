class Solution:
    def mySqrt(self, x: int) -> int:
        bot = 0
        top = x
        r = 0

        while bot <= top :
            c = bot + (top - bot) // 2
            if c * c > x :
                top = c - 1
            elif c * c < x :
                bot = c + 1
                r = c
            else :
                return c
        return r