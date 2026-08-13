class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        minHeap = []

        for i,(a,b)in enumerate(workers):
            for j,(c,d) in enumerate(bikes):
                dist = abs(a-c) + abs(b-d)

                heapq.heappush(minHeap,(dist,i,j))

        arr = [0]*len(workers)
        wSet = set()
        bSet = set()

        while minHeap and len(wSet) < len(workers):
            dist,worker,bike = heapq.heappop(minHeap)
            if worker in wSet or bike in bSet:
                continue

            arr[worker] = bike
            wSet.add(worker)
            bSet.add(bike)

        return arr


