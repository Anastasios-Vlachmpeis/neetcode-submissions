class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        l = amount+1
        a = l*[0]

        if amount == 0:
            return 0

        for i in range(l) :

            for c in coins :
                if i - c == 0 : 
                    a[i] = 1
            
                elif i - c > 0 and a[i-c] > 0 :
                    if a[i] == 0:
                        a[i] += a[i - c] + 1
                    else :
                        a[i] = min(a[i], a[i-c] + 1)    
        
        return -1 if a[l-1] == 0 else a[l-1]


