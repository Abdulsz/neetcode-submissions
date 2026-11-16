class FreqStack:

    def __init__(self):
        
        self.maxFreq = 0
        self.freq = {}
        self.group = defaultdict(list)

    def push(self, val: int) -> None:
        
        self.freq[val] = 1+ self.freq.get(val,0)
        f = self.freq[val]

        self.group[f].append(val)
        self.maxFreq = max(self.maxFreq,f)

    def pop(self) -> int:

        top = self.group[self.maxFreq].pop()
        self.freq[top]-=1
        if not self.group[self.maxFreq]:
            self.maxFreq-=1
        return top

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()