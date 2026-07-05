class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP = 0 
        lo = 101
        for i in range(len(prices)) :
            lo = min(lo,prices[i])
            mP = max(prices[i] - lo,mP)
        return mP