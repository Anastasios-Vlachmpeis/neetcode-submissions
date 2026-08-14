class Solution:
    def isValid(self, s: str) -> bool:
        lib1 = ["{","[","("]
        lib2 = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        st = []
        for i in s :
            if i in lib1 :
                st.append(i)
            else :
                if not st or lib2[i] is not st.pop():
                    return False
        return not st