class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks)<=1:
            return 0
        heapq.heapify(sticks)
        totalCost = 0
        while len(sticks)>1:
            fst = heapq.heappop(sticks)
            snd = heapq.heappop(sticks)

            heapq.heappush(sticks,fst+snd)
            totalCost += fst+snd

        return totalCost
        
        