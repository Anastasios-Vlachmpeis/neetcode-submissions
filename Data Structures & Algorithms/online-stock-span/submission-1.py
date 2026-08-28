class StockSpanner:

    def __init__(self):
        self.d = {}
        self.li = []


    def next(self, price: int) -> int:
        self.li.append(price)
        i = len(self.li) - 2
        c = 1
        while i >= 0 and self.li[i] <= self.li[-1] :
            c += self.d[self.li[i]]
            i -= self.d[self.li[i]]
        self.d[price] = c
        return self.d[price]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)