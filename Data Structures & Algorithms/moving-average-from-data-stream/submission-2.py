class MovingAverage:

    def __init__(self, size: int):
        self.n = 0
        self.curSum = 0
        self.q = deque()
        self.size = size

    def next(self, val: int) -> float:
        self.q.append(val)
        self.curSum+=val
        
        if len(self.q) > self.size:
            self.curSum -= self.q.popleft()
            self.n-=1
        
        self.n+=1
        return self.curSum/self.n
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
