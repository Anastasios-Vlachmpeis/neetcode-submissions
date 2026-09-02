class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        lr = len(grid)
        lc = len(grid[0])
        r,c = 0,0
        for i in range(lr) :
            for j in range(lc) :
                if grid[i][j] == 1:
                    r,c = i,j
                    break
        
                    
        def rec(i, j) :
            if i >= lr or j >= lc or j < 0 or i < 0 or grid[i][j] == 0:
                return 1
            if (i,j) in seen :
                return 0
            seen.add((i,j))
            return rec(i,j+1) + rec(i+1,j) + rec(i-1,j) + rec(i,j-1)

        return rec(r, c)


