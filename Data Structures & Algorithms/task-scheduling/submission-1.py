class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        q = deque()
        count = Counter(tasks)

        minHeap = []
        for key,val in count.items():
            heapq.heappush(minHeap,-val)
        time = 0
        while minHeap or q:
            
            time+=1
            if minHeap:
                cnt = heapq.heappop(minHeap)
                cnt+=1
                if cnt!=0:
                    q.append((time+n,cnt))

            if q and q[0][0] <= time:
                _,cnt = q.popleft()
                heapq.heappush(minHeap, cnt)

        return time


                

