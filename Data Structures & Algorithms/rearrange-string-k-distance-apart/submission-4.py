class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        count =Counter(s)
        q = deque()
        time = 0
        maxHeap = []

        for a,b in count.items():
            heapq.heappush(maxHeap,(-b,a))

        res = []
        while maxHeap or q:

            if q and q[0][0] <= time:
                t,cnt,char = q.popleft()
                heapq.heappush(maxHeap,(cnt,char))
            
            if not maxHeap:
                return ""

 
            cnt,char = heapq.heappop(maxHeap)
            res.append(char)
            cnt+=1
            if cnt < 0:
                q.append((time+k,cnt,char))
            time+=1

        return "".join(res)

            




        