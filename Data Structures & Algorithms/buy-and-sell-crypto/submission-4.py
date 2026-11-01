class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previous_min = 101
        diff = 0

        for price in prices :
            diff = max(diff, price - previous_min)
            previous_min = min(previous_min, price)

        return diff