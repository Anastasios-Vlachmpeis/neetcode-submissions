class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            "}":"{","]":"[",")":"("
        }
        se = ["}","]",")"]

        for i in s:
            if i in se :
                if not stack:
                    return False
                if stack.pop() == dic[i]:
                    continue
                return False
            else:
                stack.append(i)
        
        return not stack