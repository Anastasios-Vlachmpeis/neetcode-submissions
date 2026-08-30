class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1 :
            s1 = stones.pop()
            s2 = stones.pop()
            print(s1,s2)

            if abs(s1 - s2) > 0 :
                heapq.heappush(stones,abs(s1 - s2))
        
        return 0 if len(stones) == 0 else stones[0]