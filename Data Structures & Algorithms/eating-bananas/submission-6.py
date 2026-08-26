class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bot = 1
        top = max(piles)
        m = top

        def ch(i,j) :
            if i % j == 0 :
                return 0
            return 1

        while top >= bot :
            cur = bot + (top - bot) // 2
            req = 0

            for i in piles :
                
                req += (i // cur + ch(i,cur)) if cur < i else + 1
                #print("B", req, i, cur)
            if req <= h :
                m = cur
                top = cur - 1
            else :
                bot = cur + 1
            
        return m