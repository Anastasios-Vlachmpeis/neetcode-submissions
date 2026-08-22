class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        st = set()
        if k == 0 :
            return False
        
        for i in range(k) :
            if nums[i] in st:
                return True
            st.add(nums[i])
            

        for i in range(k,l) :
            
            prev = nums[i-k]
            
            if nums[i] in st :
                return True
            st.remove(prev)
            
            st.add(nums[i])

        return False
