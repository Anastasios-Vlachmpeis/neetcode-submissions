class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return " 0 "
        sTs = ""
        for i in range(len(strs)):
            if i < len(strs) - 1:
                sTs += strs[i] + "HaKuNa"
            else:
                sTs += strs[i]
        return sTs

    def decode(self, s: str) -> List[str]:
        
        if s == " 0 ":
            sTss = []
        else:
            sTss = s.split("HaKuNa")
        return sTss