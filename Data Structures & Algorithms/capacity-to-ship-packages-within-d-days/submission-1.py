class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        bot = max(weights)
        top = sum(weights)
        bday = top

        while bot <= top :
            c = bot + (top - bot) // 2
            cdays = 1
            cship = 0
            
            for package in weights :
                if cship + package > c :
                    cdays += 1
                    cship = 0
            
                cship += package
            
            if cdays <= days :
                top = c - 1
                bday = min(c,bday)
            
            else :
                bot = c + 1

        return bday

        
