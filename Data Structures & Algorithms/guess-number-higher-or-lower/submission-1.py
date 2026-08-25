# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        top = n
        bot = 1

        while bot <= top :
            i = bot + (top - bot) // 2
            g = guess(i)

            if g == 0 :
                return i
            elif g == -1 :
                top = i - 1
            else :
                bot = i + 1
