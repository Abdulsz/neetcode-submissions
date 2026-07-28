class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = deque()
        self.total = 0

    def next(self, val: int) -> float:

        self.arr.append(val)
        self.total+=val
        if len(self.arr) > self.size:
            pop = self.arr.popleft()
            self.total-=pop
        return self.total/len(self.arr)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
