class MinStack:

    def __init__(self):
        self.min = []
        self.mi = -1
        self.stack = []
        self.t = -1

    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        elif self.min[self.mi] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[self.mi])
        self.mi += 1
        self.t += 1
        self.stack.append(val)

    def pop(self) -> None:
        self.t -= 1
        self.mi -= 1
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[self.t]

    def getMin(self) -> int:
        return self.min[self.mi]
