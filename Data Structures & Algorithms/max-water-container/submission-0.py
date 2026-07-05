class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxW = 0
        runW = 0

        while i < j :
            runW = min(heights[i]* (j-i),heights[j] * (j-i))
            if maxW < runW:
                maxW = runW
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return maxW