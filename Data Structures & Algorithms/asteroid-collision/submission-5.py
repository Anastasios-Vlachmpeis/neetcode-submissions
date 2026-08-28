class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids :
            if not s :
                s.append(i)
            else :
                s.append(i)
                while len(s) >= 2 and s[-1] * s[-2] < 0:
                    if s[-2] < s[-1] :
                        break 
                    elif abs(s[-1]) == abs(s[-2]):
                        s.pop()
                        s.pop()
                        break
                    elif abs(s[-2]) > abs(s[-1]) :
                        s.pop()
                        break
                    elif abs(s[-2]) < abs(s[-1]) :
                        s[-2] = s[-1]
                        s.pop()
        return s