class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in range(len(operations)) :
            if operations[i] == "+" :
                s.append(int(s[-1]) + int(s[-2]))
            elif operations[i] == "D" :
                s.append(int(s[-1]) * 2)
            elif operations[i] == "C" :
                s.pop()
            else :
                s.append(int(operations[i]))

        return sum(s)