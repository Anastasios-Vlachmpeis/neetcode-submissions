class Solution:
    def integerBreak(self, n: int) :
        m = -1
        if n == 2 or n == 3 :
            return n - 1

        for i in range(1,n - 1) :
            md = n % i
            x = (n - md ) // i
            curr = x
            count = 1

            while curr + md < n:
                curr += x
                count += 1

            if md >= 1 :
                print(md + i)
                mdmax = (md + i)

                for j in range (1,(md + x) -1) :
                    x2 = (md + i) // j
                    mdmax = max(mdmax,x2 * (md + i - x2) )
                x -= 1
                md = mdmax
            else :
                md = 1
            m = max(m, md * i ** x )
        return m