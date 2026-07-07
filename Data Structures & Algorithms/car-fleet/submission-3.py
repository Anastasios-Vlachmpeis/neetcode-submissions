class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = {}

        for i in range(len(position)):
            m[position[i]] = (target - position[i]) / speed[i]

        position.sort(reverse = True)
        
        
        po = []
        j = -1

        for i in range(len(position)) :
            if j >= 0:
                
                if m[po[j]] > m[position[i]]:
                    m[position[i]]= m[po[j]]

            po.append(position[i])
            j += 1

        return len(list(set(m.values())))