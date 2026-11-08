class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        maxHeap = []
        for cnt,c in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if cnt !=0:
                heapq.heappush(maxHeap,(cnt,c))
        
        res =[]
        
        while maxHeap:

            cnt,char = heapq.heappop(maxHeap)
            if len(res)>1 and res[-1]==res[-2]==char:

                if not maxHeap:
                    break

                cnt2,char2 = heapq.heappop(maxHeap)
                cnt2+=1

                res.append(char2)
                if cnt2:
                    heapq.heappush(maxHeap,(cnt2,char2))

            else:
                res.append(char)
                cnt+=1
            if cnt:
                heapq.heappush(maxHeap,(cnt,char))

        return "".join(res)
