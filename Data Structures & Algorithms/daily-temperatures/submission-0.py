class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        l = len(temperatures)
        ind = -1
        result = [0]*l

        for i in range(l) :
        
            if not st:
                st.append(i)
                ind += 1

            while ind >= 0 and temperatures[st[ind]] < temperatures[i]:
                result[st[ind]] = i - st[ind]
                st.pop()
                ind -= 1
            
            if ind < 0 or st[ind] != i:
                st.append(i)
                ind += 1
                
        return result