class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        m = ["+","*","/","-"]
        ops = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "-": lambda x, y: x - y}
        for i in tokens:
            if i in m:
                p2 = s.pop()
                p1 = s.pop()
                s.append(int(ops[i](p1,p2)))
            else :
                s.append(int(i))
        return s.pop()           
