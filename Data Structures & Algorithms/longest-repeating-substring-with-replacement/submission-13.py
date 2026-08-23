class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dt1 = {} # Current Letter index
        dt2 = {} # Current letter max in a row
        dt3 = {} # Current letter remainder
        dt4 = {} # Current letter count
        m1 = 1
        for i in range(len(s)) :
            if s[i] not in dt1 :
                dt1[s[i]] = i # When letter not present, 
                dt2[s[i]] = 1 # initialize all it's dict pointers
                dt3[s[i]] = k # remainder
                dt4[s[i]] = 1 
            else : # Otherwise, if the Δ with prev. occ <= remainder
                if i - (dt1[s[i]] + 1) <= dt3[s[i]] : 
                    dt3[s[i]] = dt3[s[i]] - (i - dt1[s[i]] - 1)
                    dt2[s[i]] = dt2[s[i]] + (i - dt1[s[i]])
                    m1 = max(m1, dt2[s[i]]) 
                else : # If not, restart
                    # dt2[s[i]] += dt3[s[i]]
                    # #print(dt2[s[i]])
                    # m1 = max(m1, dt2[s[i]])
                    dt3[s[i]] = k
                    dt2[s[i]] = 1
                    dt4[s[i]] = 0
                dt1[s[i]] = i # save current last ind
                dt4[s[i]] += 1
            
            #print(s[i])
            #print(dt1[s[i]],dt2[s[i]],dt3[s[i]],dt4[s[i]])
        #print(dt1,dt2,dt3,dt4)
        st = set(list(s))
        for i in st :
            if dt4[i] <= dt2[i] :
                if dt3[i] + dt2[i] <= len(s) :
                    m1 = max(m1, dt3[i] + dt2[i])
                else :
                    m1 =max(m1, len(s))
        #print(m1)


        dt12 = {} # Current Letter index
        dt22 = {} # Current letter max in a row
        dt32 = {} # Current letter remainder
        dt42 = {} # Current letter count
        m2 = 1
        
        for i in range(len(s)-1,-1,-1) :
            # if "S" in dt12:
            #     print(dt12["S"],dt22["S"],dt32["S"],dt42["S"])
            if s[i] not in dt12 :
                dt12[s[i]] = i # When letter not present, 
                dt22[s[i]] = 1 # initialize all it's dict pointers
                dt32[s[i]] = k # remainder
                dt42[s[i]] = 1 
            else : # Otherwise, if the Δ with prev. occ <= remainder
                #if "S" in dt12:
                    #print(f"({dt12[s[i]]}) - {i} <= {dt32[s[i]]} = {(dt12[s[i]]) - i <= dt32[s[i]]}")
                if (dt12[s[i]]) - i - 1 <= dt32[s[i]] : 
                    dt32[s[i]] = dt32[s[i]] - (dt12[s[i]] - i - 1)
                    dt22[s[i]] = dt22[s[i]] + (dt12[s[i]] - i)
                    m2 = max(m2, dt22[s[i]]) 
                else : # If not, restart
                    dt22[s[i]] += dt32[s[i]]
                    #print(dt2[s[i]])
                    m2 = max(m2, dt22[s[i]])
                    dt32[s[i]] = k
                    dt22[s[i]] = 1
                    dt42[s[i]] = 0

                dt12[s[i]] = i 
                dt42[s[i]] += 1
            
            #print(s[i])
        #print(dt12,dt22,dt32,dt42)

        st1 = set(list(s))
        # print(st1)
        #print(m2,s)
        for i in st1 :
            if dt42[i] <= dt22[i] :
                #print(dt32[i] + dt22[i])
                #print(m2,s)
                if dt32[i] + dt22[i] <= len(s) :
                    #print(m2,s)
                    m2 = max(m2, dt32[i] + dt22[i])
                    #print(dt32[i] + dt22[i])
                else :
                    
                    m2 =max(m2, len(s))
                    #print(dt32[i] + dt22[i])
        #print(m2)


        return max(m1,m2)


