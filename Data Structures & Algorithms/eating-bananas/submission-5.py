class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bot = 1
        top = max(piles)
        m = top

        while top >= bot :
            cur = bot + (top - bot) // 2
            req = 0

            for i in piles :
                req += math.ceil(float(i) / cur)
            if req <= h :
                m = cur
                top = cur - 1
            else :
                bot = cur + 1
            
        return m