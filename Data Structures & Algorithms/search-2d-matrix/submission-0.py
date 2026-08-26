class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        bot = 0
        top = n * m - 1

        while top >= bot :
            c = bot + (top - bot) // 2
            if matrix[c//n][c%n] < target :
                bot = c + 1
            elif matrix[c//n][c%n] > target :
                top = c - 1
            else :
                return True
        return False