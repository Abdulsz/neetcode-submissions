class StockSpanner:

    def __init__(self):
        
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        stack = self.stack
        while stack and stack[-1][1]<=price:
            cnt,p = stack.pop()
            span+=cnt
        
        stack.append((span,price))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)