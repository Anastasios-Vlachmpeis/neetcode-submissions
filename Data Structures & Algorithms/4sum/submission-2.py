class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)

        nums.sort()

        lists = {}

        for i in range(l) :
            for j in range(l-1,-1,-1):
                p1 = 0
                p2 = l - 1
                if i != j :
                    while p1 < p2 :
                        if p2 == i or p2 == j or nums[i] + nums[j] + nums[p1] + nums[p2] > target :
                            p2 -= 1
                        elif p1 == i or p1 == j or nums[i] + nums[j] + nums[p1] + nums[p2] < target :
                            p1 += 1
                        else :
                            li = [nums[i], nums[j], nums[p1], nums[p2]]
                            li.sort()
                            lists[tuple(li)] = li
                            p2 -= 1
                            p1 += 1

        return list(lists.values())
